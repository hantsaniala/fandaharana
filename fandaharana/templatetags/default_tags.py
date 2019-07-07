from django import template
from django.utils.translation import ugettext_lazy as _

import calendar


register = template.Library()


@register.filter
def month_name(month_number):
    return _(calendar.month_name[month_number])
