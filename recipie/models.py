from sqlite3 import TimestampFromTicks
from django.db import models
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

# Create your models here.

"""
prep time
cook time
resting time
servings

"""

class RecipieIngredient(TimeStampedModel):
    name = models.CharField("Name of Ingredient", max_length=100)
    quantity = models.CharField("quantity", max_length=10)


class RecipieDirections(TimeStampedModel):
    directions = models.CharField("directions", max_length=1024)


class Recipie(TimeStampedModel):
    name = models.CharField("Recipie name")
    slug = AutoSlugField("Recipie name", unique=True,
        always_update=False, populate_from=)
