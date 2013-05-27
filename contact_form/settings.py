from django.conf import settings

settings.CONTACT_FORM_SUCCESS = getattr(
    settings, 'CONTACT_FORM_SUCCESS', 'contact_form:completed')

settings.CONTACT_FORM_SUBECT = getattr(
    settings, 'CONTACT_FORM_SUBECT', 'Contact request received')