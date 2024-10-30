from django.urls import path
from .views import (
    food_item_list,
    food_item_create,
    food_item_update,
    food_item_delete,
    recipe_list,
)

urlpatterns = [
    path('food-items/', food_item_list, name='food_item_list'),
    path('food-items/create/', food_item_create, name='food_item_create'),
    path('food-items/update/<int:pk>/', food_item_update, name='food_item_update'),
    path('food-items/delete/<int:pk>/', food_item_delete, name='food_item_delete'),
    path('recipes/', recipe_list, name='recipe_list'),
]
