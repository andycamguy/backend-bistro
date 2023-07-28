import json
from django.http import JsonResponse
from .models import MenuItem
import os  # Import the os module to handle file paths

def bistro_items(request):
    # Get the path to the 'bistro' directory
    bistro_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the 'cuisine.json' file within the 'bistro' directory
    json_file = os.path.join(bistro_dir, 'cuisine.json')

    # Call the load_from_json function to load the data from the JSON file
    MenuItem.load_from_json(json_file)

    # Now, you can query the MenuItem objects and use them in your view
    menu_items = MenuItem.objects.all()

    menu_item_data = []
    for item in menu_items:
        item_data = {
            'name': item.name,
            'description': item.description,
            'price': float(item.price),
            'category': item.category.name,
        }
        menu_item_data.append(item_data)

    # Return the menu_item_data list as the JSON response
    return JsonResponse(menu_item_data, safe=False)