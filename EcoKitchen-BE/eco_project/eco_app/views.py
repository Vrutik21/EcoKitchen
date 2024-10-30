from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FoodItem, FoodCategory, Recipe
from .forms import FoodItemForm

@login_required
def food_item_list(request):
    """List all food items for the logged-in user."""
    food_items = FoodItem.objects.filter(user=request.user)
    return render(request, 'food_item_list.html', {'food_items': food_items})

@login_required
def food_item_create(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_item_list')
    else:
        form = FoodItemForm()
    categories = FoodCategory.objects.all()
    return render(request, 'food_item_form.html', {'form': form, 'categories': categories})

@login_required
def food_item_update(request, pk):
    food_item = get_object_or_404(FoodItem, pk=pk)
    if request.method == 'POST':
        form = FoodItemForm(request.POST, instance=food_item)
        if form.is_valid():
            form.save()
            return redirect('food_item_list')
    else:
        form = FoodItemForm(instance=food_item)
    categories = FoodCategory.objects.all()
    return render(request, 'food_item_form.html', {'form': form, 'categories': categories})

@login_required
def food_item_delete(request, pk):
    """Delete a food item."""
    food_item = get_object_or_404(FoodItem, pk=pk, user=request.user)
    if request.method == 'POST':
        food_item.delete()
        return redirect('food_item_list')
    return render(request, 'food_item_confirm_delete.html', {'food_item': food_item})

@login_required
def recipe_list(request):
    """List all recipes."""
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})
