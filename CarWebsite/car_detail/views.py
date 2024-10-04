from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Car

# View to list all cars
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_detail/car_list.html', {'cars': cars})

# View to add a car (only for logged-in users)
@login_required
def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        model = request.POST.get('model')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        car = Car(name=name, model=model, price=price, description=description, image=image)
        car.save()
        return redirect('car_list')
    return render(request, 'car_detail/add_car.html')

# View to handle signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
