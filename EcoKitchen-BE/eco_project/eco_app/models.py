from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class FoodCategory(models.Model):
    "Category of the food item, e.g., Dairy, Vegetables, Fruits, etc."
    name = models.CharField(max_length=50, unique=True)

    def _str_(self):
        return self.name

class FoodItem(models.Model):
    "Model for food items in the user's inventory."
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="food_items")
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(help_text="Quantity of the item")
    unit = models.CharField(max_length=50, help_text="Unit for quantity, e.g., kg, pieces")
    added_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(help_text="Expiration date of the food item")
    is_expired = models.BooleanField(default=False)

    def _str_(self):
        return f"{self.name} - {self.user.username}"

    def check_expiration(self):
        "Mark item as expired if past expiration date."
        if self.expiration_date < timezone.now().date():
            self.is_expired = True
            self.save()

class Recipe(models.Model):
    "Model for storing recipe suggestions."
    name = models.CharField(max_length=200, unique=True)
    ingredients = models.TextField(help_text="Ingredients required for the recipe")
    instructions = models.TextField(help_text="Instructions for preparing the recipe")

    def _str_(self):
        return self.name

class SuggestedRecipe(models.Model):
    "Model for storing recipe suggestions based on user's inventory."
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="suggested_recipes")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    suggested_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.recipe.name} - {self.user.username}"

class ExpirationNotification(models.Model):
    "Model to handle notifications for expiring items."
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="notifications")
    notified_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    def _str_(self):
        return f"Notification for {self.food_item.name} - {self.user.username}"