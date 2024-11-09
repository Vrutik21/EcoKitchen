from django.contrib import admin
from .models import FoodCategory, FoodItem, Recipe, SuggestedRecipe, ExpirationNotification,CustomUser

admin.site.register(FoodCategory)
admin.site.register(FoodItem)
admin.site.register(Recipe)
admin.site.register(SuggestedRecipe)
admin.site.register(ExpirationNotification)

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    search_fields = ['email', 'username']

admin.site.register(CustomUser, CustomUserAdmin)