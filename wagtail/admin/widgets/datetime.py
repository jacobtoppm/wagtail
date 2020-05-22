import json

from django import forms
from django.conf import settings
from django.forms import widgets
from django.utils.formats import get_format

from wagtail.admin.datetimepicker import to_datetimepicker_format
from wagtail.admin.staticfiles import versioned_static


DEFAULT_DATE_FORMAT = '%Y-%m-%d'
DEFAULT_TIME_FORMAT = '%H:%M'
DEFAULT_DATETIME_FORMAT = '%Y-%m-%d %H:%M'


class AdminDateInput(widgets.DateInput):
    template_name = 'wagtailadmin/widgets/date_input.html'

    def __init__(self, attrs=None, format=None):
        default_attrs = {'autocomplete': 'new-date'}
        fmt = format
        if attrs:
            default_attrs.update(attrs)
        if fmt is None:
            if getattr(settings, 'USE_L10N', False):
                fmt = get_format('DATE_INPUT_FORMATS')[0]
            else:
                fmt = getattr(settings, 'WAGTAIL_DATE_FORMAT', DEFAULT_DATE_FORMAT)
        self.js_format = to_datetimepicker_format(fmt)
        super().__init__(attrs=default_attrs, format=fmt)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        config = {
            'dayOfWeekStart': get_format('FIRST_DAY_OF_WEEK'),
            'format': self.js_format,
        }
        context['widget']['config_json'] = json.dumps(config)

        return context

    @property
    def media(self):
        return forms.Media(js=[
            versioned_static('wagtailadmin/js/date-time-chooser.js'),
        ])


class AdminTimeInput(widgets.TimeInput):
    template_name = 'wagtailadmin/widgets/time_input.html'

    def __init__(self, attrs=None, format=None):
        default_attrs = {'autocomplete': 'new-time'}
        if attrs:
            default_attrs.update(attrs)
        fmt = format
        if fmt is None:
            if getattr(settings, 'USE_L10N', False):
                fmt = get_format('TIME_INPUT_FORMATS')[0]
            else:
                fmt = getattr(settings, 'WAGTAIL_TIME_FORMAT', DEFAULT_DATETIME_FORMAT)
        self.js_format = to_datetimepicker_format(fmt)
        super().__init__(attrs=default_attrs, format=fmt)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        config = {
            'format': self.js_format,
            'formatTime': self.js_format
        }
        context['widget']['config_json'] = json.dumps(config)

        return context

    @property
    def media(self):
        return forms.Media(js=[
            versioned_static('wagtailadmin/js/date-time-chooser.js'),
        ])


class AdminDateTimeInput(widgets.DateTimeInput):
    template_name = 'wagtailadmin/widgets/datetime_input.html'

    def __init__(self, attrs=None, format=None, time_format=None):
        default_attrs = {'autocomplete': 'new-date-time'}
        fmt = format
        if attrs:
            default_attrs.update(attrs)
        if fmt is None:
            if getattr(settings, 'USE_L10N', False):
                fmt = get_format('DATETIME_INPUT_FORMATS')[0]
            else:
                fmt = getattr(settings, 'WAGTAIL_DATETIME_FORMAT', DEFAULT_DATETIME_FORMAT)
        time_fmt = time_format
        if time_fmt is None:
            if getattr(settings, 'USE_L10N', False):
                time_fmt = get_format('TIME_INPUT_FORMATS')[0]
            else:
                time_fmt = getattr(settings, 'WAGTAIL_TIME_FORMAT', DEFAULT_TIME_FORMAT)
        self.js_format = to_datetimepicker_format(fmt)
        self.js_time_format = to_datetimepicker_format(time_fmt)
        super().__init__(attrs=default_attrs, format=fmt)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        config = {
            'dayOfWeekStart': get_format('FIRST_DAY_OF_WEEK'),
            'format': self.js_format,
            'formatTime': self.js_time_format
        }
        context['widget']['config_json'] = json.dumps(config)

        return context

    @property
    def media(self):
        return forms.Media(js=[
            versioned_static('wagtailadmin/js/date-time-chooser.js'),
        ])
