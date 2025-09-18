from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from .models import Customer,Restaurant

def index(request):
    return render(request, 'index.html')

def signIn(request):
    return render(request, 'signIn.html')

def signUp(request):
    return render(request, 'signUp.html')

def osignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        try:
            Customer.objects.get(username=username)
            return HttpResponse("Duplicates Not Allowed")
        except:
            Customer.objects.create(
                username=username,
                email=email,
                password=password,
                phone=phone,
                address=address
            )
        
    return render(request, 'signIn.html')

def osignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            customer = Customer.objects.get(username=username, password=password)
            if username == "admin":
                return render(request, "admin_home.html", {"customer": customer})
            else:
                return render(request, "customer_home.html", {"customer": customer})
        except Customer.DoesNotExist:
            return render(request, "fail.html")

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        Restaurant.objects.create(
            name=name,
            picture=picture,
            cuisine=cuisine,
            rating=rating
        )
        return redirect('show_restaurant')
    return render(request, "add_restaurant.html")


def show_restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, "show_restaurant.html", {"restaurants": restaurants})

def update_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == "POST":
        restaurant.name = request.POST.get("name")
        restaurant.picture = request.POST.get("picture")
        restaurant.cuisine = request.POST.get("cuisine")
        restaurant.rating = request.POST.get("rating")
        restaurant.save()
        messages.success(request, f"{restaurant.name} updated successfully! ✅")
        return redirect("show_restaurant")
    return render(request, "update_restaurant.html", {"restaurant": restaurant})

def delete_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == "POST":
        restaurant.delete()
        messages.success(request, "Restaurant deleted successfully 🗑")
        return redirect("show_restaurant")
    return redirect("show_restaurant")