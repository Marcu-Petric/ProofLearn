from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the new user to the database
            # Optionally log the user in immediately
            login(request, user)
            
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")
            return redirect('home')  # Replace 'home' with the name of your desired redirect URL
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})