from django.forms import CharField, ChoiceField
from django.core.exceptions import ValidationError
import re

# List of all Irish counties
IRISH_COUNTIES = [
    ("CW", "Carlow"),
    ("CN", "Cavan"),
    ("CE", "Clare"),
    ("C", "Cork"),
    ("DL", "Donegal"),
    ("D", "Dublin"),
    ("G", "Galway"),
    ("KY", "Kerry"),
    ("KE", "Kildare"),
    ("KK", "Kilkenny"),
    ("LS", "Laois"),
    ("LM", "Leitrim"),
    ("LK", "Limerick"),
    ("LD", "Longford"),
    ("LH", "Louth"),
    ("MO", "Mayo"),
    ("MH", "Meath"),
    ("MN", "Monaghan"),
    ("OY", "Offaly"),
    ("RN", "Roscommon"),
    ("SO", "Sligo"),
    ("TY", "Tipperary"),
    ("WD", "Waterford"),
    ("WH", "Westmeath"),
    ("WX", "Wexford"),
    ("WW", "Wicklow"),
]

# Validator for Irish Eircode
def validate_eircode(value):
    
#This validates the Irish Eircode in format: 'A65 F4E2'

    pattern = r"^[A-Za-z0-9]{3}[ ]?[A-Za-z0-9]{4}$"
    if not re.match(pattern, value):
        raise ValidationError(f"{value} is not a valid Eircode.")

# Irish Eircode Field
class IrishEircodeField(CharField):
    
#Custom form field for Irish Eircode validation.
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 8
        kwargs['validators'] = [validate_eircode]
        super().__init__(*args, **kwargs)

# Irish County Field
class IrishStateField(ChoiceField):
    
#Custom form field for Irish County selection.
    
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = IRISH_COUNTIES
        super().__init__(*args, **kwargs)
