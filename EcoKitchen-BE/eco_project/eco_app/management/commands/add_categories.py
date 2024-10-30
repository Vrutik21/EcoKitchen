from django.core.management.base import BaseCommand
from eco_app.models import FoodCategory

class Command(BaseCommand):
    help = 'Add example food categories to the database'

    def handle(self, *args, **kwargs):
        categories = [
            "Dairy",
            "Vegetables",
            "Fruits",
            "Grains",
            "Meat",
            "Seafood",
            "Beverages",
            "Snacks",
        ]

        for category in categories:
            FoodCategory.objects.get_or_create(name=category)
            self.stdout.write(self.style.SUCCESS(f'Added category: {category}'))
