import re
from django.core.exceptions import ValidationError


def validate(value):
    symbols = ['!', '@', '#', '$', '%', '&', '*', '^']
    flag = 0
    u = 0
    l = 0

    for i in value:
        if(i in symbols):
            flag = 1
            break

    if(flag == 0):
        raise ValidationError("Atleast one symbol (!,@,#,$,%,^,&,*) should be present")

    if(len(value) < 9):
        raise ValidationError("A minimum of 9 characters should be present in the password")

    for i in value:
        if(i.isupper()):
            u += 1
        elif(i.islower()):
            l += 1

    if(u == 0):
        raise ValidationError("Atleast 1 uppercase letter should be present")

    if(l == 0):
        raise ValidationError("Atleast 1 lowercase letter should be present")
