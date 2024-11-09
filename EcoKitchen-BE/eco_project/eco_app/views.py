from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import FoodItem, FoodCategory, Recipe
from .forms import FoodItemForm
from django.contrib.auth import get_user_model,authenticate
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

User = get_user_model()

class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            })
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": "Welcome to Eco Kitchen"})

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
