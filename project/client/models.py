from django.db import models
from django.core.exceptions import ValidationError
import re
from client.word_wrapper import RandWord
from amazon.amazon_wrapper import AMZN
from giphy.wrapper import AmGiphy
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
    # rounds = models.IntegerField()
    # giphy_score = models.IntegerField()
    # amazon_score = models.IntegerField()
    
    # def add_round_count(self):
    #     self.round += 1

    # def add_giphy_count(self):
    #     self.giphy_score +=1
    #
    # def add_amazon_score(self):
    #     self.amazon_score +=1
