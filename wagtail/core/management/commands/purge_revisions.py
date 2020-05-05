from django.core.management.base import BaseCommand
from django.utils import timezone

from wagtail.core.models import PageRevision

try:
    from wagtail.core.models import WorkflowState
    workflow_support = True
except ImportError:
    workflow_support = False


class Command(BaseCommand):
    help = 'Delete page revisions which are not the latest revision for a page, published or scheduled to be published, or in moderation'

    def add_arguments(self, parser):
        parser.add_argument('--days', type=int, help="Only delete revisions older than this number of days")

    def handle(self, *args, **options):
        days = options.get('days')

        revisions_deleted = purge_revisions(days=days)

        if revisions_deleted:
            self.stdout.write(self.style.SUCCESS('Successfully deleted %s revisions' % revisions_deleted))
        else:
            self.stdout.write("No revisions deleted")


def purge_revisions(days=None):
    # exclude revisions which have been submitted for moderation in the old system
    purgable_revisions = PageRevision.objects.exclude(
        submitted_for_moderation=True
    ).exclude(
        # and exclude revisions with an approved_go_live_at date
        approved_go_live_at__isnull=False)

    if workflow_support:
        purgable_revisions = purgable_revisions.exclude(
            # and exclude revisions linked to an in progress workflow state
            task_states__workflow_state__status=WorkflowState.STATUS_IN_PROGRESS
        )

    if days:
        purgable_until = timezone.now() - timezone.timedelta(days=days)
        # only include revisions which were created before the cut off date
        purgable_revisions = purgable_revisions.filter(created_at__lt=purgable_until)

    deleted_revisions_count = 0

    for revision in purgable_revisions:
        # don't delete the latest revision for any page
        if not revision.is_latest_revision():
            revision.delete()
            deleted_revisions_count += 1

    return deleted_revisions_count
