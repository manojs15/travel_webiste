from django.shortcuts import redirect,render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.middleware.csrf import rotate_token  

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:log')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']     

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User is authenticated, log them in
            login(request, user)
            return redirect('home:home')  # Redirect to home page after successful login
        else:
            # Authentication failed, render login form with error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error': error_message})

    # If the request method is not POST, render the login form
    return render(request, 'login.html')