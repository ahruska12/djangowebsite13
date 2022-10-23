from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, ProductInstance, Categories, OrderItem, Order, Profile


def index(request):
    num_products = Product.objects.count()
    num_instances = ProductInstance.objects.count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_products': num_products,
        'num_instances': num_instances,
    }

    return render(request, 'index.html', context=context)


class AllProductsListView(generic.ListView):
    model = Product


class ProductDetailView(generic.DetailView):
    model = Product


def music_list(request):
    product = Product.objects.filter()
    return render(request, 'store/all_music_list.html',
                  {'all-music': product})

def merch_list(request):
    product = Product.objects.filter()
    return render(request, 'store/all_merch_list.html',
                  {'all-merch': product})

def contact_us(request):
    return render(request, 'contactus.html')

def cart_add(request, prod_id):
    item = Product.objects.get(pk=prod_id)
    return render('shopping_cart.html')




#Sale Items Page
def sale_items(request):
    product = Product.objects.filter()
    return render(request, 'store/sale_items.html',
                  {'sale-items': product})


def wish_list(request):
    product = Product.objects.filter()
    return render(request, 'store/wish_list.html',
                  {'wish-list': product})


#I want to change this to import the user instead of the product but I am not sure what pycharm calls the user class
def user_profile_settings(request):
    product = Product.objects.filter()
    return render(request, 'store/user_profile_settings.html',
                  {'user-profile-settings': product})