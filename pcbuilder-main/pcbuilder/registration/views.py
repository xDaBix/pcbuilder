from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm  # Import your newly created form

def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # This saves the user data to the database
            login(request, user)  # Log the user in automatically
            return redirect('reg')  # Redirect to the home page after successful registration
    else:
        form = UserForm()
    return render(request, 'registration/reg.html', {'form': form})
