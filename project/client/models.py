from django.db import models
from django.core.exceptions import ValidationError
import re
# Create your models here.

class Client(models.Model):
    def validate_name(submitted_name):
        if Client.objects.filter(name=submitted_name):
            raise ValidationError("This name is already taken.")
        if not re.match(r'[a-zA-Z]+[a-z0-9A-Z]{3,20}', submitted_name):
            raise ValidationError("Name must start with a letter and contain only alphanumeric keys.")

    def validate_password(submitted_password):
        if not re.match(r'[a-zA-Z]+[a-z0-9A-Z]{7,20}', submitted_password):
            raise ValidationError("Password must be between 7 and 20 alphanumeric characters.")

    name = models.CharField(max_length=255,unique=True,validators=[validate_name])
    password = models.CharField(max_length=255,validators=[validate_password])
    created_at = models.DateTimeField(auto_now_add=True)
    # key = models.CharField(max_length=32)
