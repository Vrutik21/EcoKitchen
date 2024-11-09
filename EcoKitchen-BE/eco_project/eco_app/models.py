from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.conf import settings

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class FoodCategory(models.Model):
    """Category of the food item, e.g., Dairy, Vegetables, Fruits, etc."""
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    """Model for food items in the user's inventory."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="food_items")
    name = models.CharField(max_length=100)
    category = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.PositiveIntegerField(help_text="Quantity of the item")
    unit = models.CharField(max_length=50, help_text="Unit for quantity, e.g., kg, pieces")
    added_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateField(help_text="Expiration date of the food item")
    is_expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.user.email}"

    def check_expiration(self):
        """Mark item as expired if past expiration date."""
        if self.expiration_date < timezone.now().date():
            self.is_expired = True
            self.save()

class Recipe(models.Model):
    """Model for storing recipe suggestions."""
    name = models.CharField(max_length=200, unique=True)
    ingredients = models.TextField(help_text="Ingredients required for the recipe")
    instructions = models.TextField(help_text="Instructions for preparing the recipe")

    def __str__(self):
        return self.name

class SuggestedRecipe(models.Model):
    """Model for storing recipe suggestions based on user's inventory."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="suggested_recipes")
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    suggested_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipe.name} - {self.user.email}"

class ExpirationNotification(models.Model):
    """Model to handle notifications for expiring items."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="notifications")
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, related_name="notifications")
    notified_date = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)

    def __str__(self):
        return f"Notification for {self.food_item.name} - {self.user.email}"
