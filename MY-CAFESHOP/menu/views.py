from django.shortcuts import render, redirect
from .models import MenuItem, Order

def home(request):
    return render(request, 'menu/home.html')

def menu_list(request):
    items = MenuItem.objects.all()
    return render(request, 'menu/menu.html', {'items': items})

def gallery(request):
    return render(request, 'menu/gallery.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        item = request.POST.get("item")
        message = request.POST.get("message")
        Order.objects.create(
            customer_name=name,
            email=email,
            phone=phone,
            item=item,
            message=message
        )
     

        return redirect('home')
    return render(request, 'menu/contact.html')

def about(request):
    return render(request, 'menu/about.html')

def special(request):
    return render(request, "menu/special.html")

def book_table(request):
    return render(request, "menu/book_table.html")

