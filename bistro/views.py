import json
from django.http import HttpResponse
from .models import MenuItem

def bistro_items(request):
    # Replace 'bistro/cuisine.py' with the actual path of your JSON file
    json_file = 'bistro/cuisine.py'
    
    # Read the JSON data from the file
    with open(json_file) as f:
        data = json.load(f)

    # Call the load_from_json function to load the data into the database
    MenuItem.load_from_json(data)

    # Now, you can query the MenuItem objects and use them in your view
    menu_items = MenuItem.objects.all()

    # For simplicity, let's return the names of the menu items as a response
    menu_item_names = ', '.join(item.name for item in menu_items)
    return HttpResponse(f"Menu Items: {menu_item_names}")
