from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import random
import string
from .forms import Profileform
from .models import Profile

from ProductManagement.models import Cart

v_code = '123'

# Create your views here.

def register(request):
    #creating an empty form for user registration
    form = UserCreationForm()

    # after submit button in the HTML page
    if request.method == "POST":
        # filling out the form with the inserted data from HTML page
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if valid then save to database
            user = form.save()

            # create a new cart for new user
            cart = Cart(user = user)
            cart.save()

            # after a successful registration you can redirect to any page
            return redirect('products_list')

    context={
        'form' : form
    }

    return render(request, 'UserManagement/register.html', context)

@login_required
def CreateProfile(request):
    form = Profileform()
    if request.method == "POST":
        form = Profileform(request.POST, request.FILES)

    if form.is_valid():
        profile_object = form.save(commit=False)
        profile_object.user = request.user
        profile_object.save()
        return redirect('/')
    try:
        value = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        value = '0'
    context = {
        'val': value,
        'form': form,
    }
    return render(request, 'UserManagement/create_profile.html', context)


def ViewProfile(request):
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = print("Please complete your Profile to view")
    context = {
        'profile': profile,
    }
    return render(request, 'UserManagement/view_profile.html', context)


