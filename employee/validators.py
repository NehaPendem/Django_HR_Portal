from django.core.exceptions import ValidationError


def validate_number(value):
    value = str(value)

    if(len(value) != 10):
        raise ValidationError("Please enter valid Phone Number")


def validate_skills(value):
    if(len(value) > 5):
        raise ValidationError("Please enter a max of 5 skills only")
