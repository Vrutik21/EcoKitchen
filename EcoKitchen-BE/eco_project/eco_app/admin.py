from django.contrib import admin
from .models import FoodCategory, FoodItem, Recipe, SuggestedRecipe, ExpirationNotification

admin.site.register(FoodCategory)
admin.site.register(FoodItem)
admin.site.register(Recipe)
admin.site.register(SuggestedRecipe)
admin.site.register(ExpirationNotification)
