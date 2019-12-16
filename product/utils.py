from django.utils.translation import gettext as _


def validate_fields(params):
    if params.get('price') and type(params.get('price')) is float:
        return True
    else:
        return _('Price invalid')
