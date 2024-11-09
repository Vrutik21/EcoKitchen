from django.urls import path
from .views import (
    food_item_list,
    food_item_create,
    food_item_update,
    food_item_delete,
    recipe_list,
    SignupView,
    LoginView,
    protected_view
)

urlpatterns = [
    path("", protected_view, name="protected"),
    path("signup", SignupView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path('food-items/create', food_item_create, name='food_item_create'),
    path('food-items/update/<int:pk>', food_item_update, name='food_item_update'),
    path('food-items/delete/<int:pk>', food_item_delete, name='food_item_delete'),
    path('recipes', recipe_list, name='recipe_list'),
]
