from django.shortcuts import get_object_or_404
from products.models import Product

"""
Unlike the products app where a model was created which then puts products 
into the database, in this case the cart items will not go into the database.
They will just be stored in the session when the user is logged in. 
So a user can add products to their cart but when they log out that cart will be lost. 
This is going to allow anything that is added to the cart to be available 
for display on any web page within the web app. 
So whereas before, 'all products view' was only able to 
take products and because the products into a dictionary within the 
render and that's actually more properly called a context. 
So in this case, a contect is created that is available to all pages
"""

def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering every page
    """