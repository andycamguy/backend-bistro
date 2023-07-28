from django.db import models
import json

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def load_from_json(cls, file_path):
        with open(file_path) as f:
            data = json.load(f)

        for item_data in data.get("cuisines", []):
            category_name = item_data.get("category", "")
            category, _ = Category.objects.get_or_create(name=category_name)

            MenuItem.objects.update_or_create(
                name=item_data.get("name", ""),
                defaults={
                    "description": item_data.get("description", ""),
                    "price": item_data.get("price", 0),
                    "category": category,
                },
            )
