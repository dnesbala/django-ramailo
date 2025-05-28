from django.db import models

from ramailo.models.base import BaseModel

class Category(BaseModel):
    class CategoryChoices(models.TextChoices):
        TECHNOLOGY = 'TECH', 'Technology'
        LIFESTYLE = 'LIFE', 'Lifestyle'
        TRAVEL = 'TRAV', 'Travel'
        FOOD = 'FOOD', 'Food'
        HEALTH = 'HEAL', 'Health'
        BUSINESS = 'BUSI', 'Business'
        OTHER = 'OTHR', 'Other'

    name = models.CharField(
        max_length=4,
        choices=CategoryChoices.choices,
        default=CategoryChoices.OTHER
    )
    
    def __str__(self):
        return f"Category({self.name})"