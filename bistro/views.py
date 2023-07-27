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

    # For simplicity, let's return the names of the menu items as a response
    menu_item_names = ', '.join(item.name for item in menu_items)
    return JsonResponse(f"Menu Items: {menu_item_names}", safe=False)
