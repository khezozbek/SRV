from django.shortcuts import render
import subprocess
import os

def create_linux_user(username):
    try:
        subprocess.run(['useradd', username], check=True)
        home_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'user_data', username)
        subprocess.run(['mkdir', '-p', home_directory], check=True)
        subprocess.run(['chown', f'{username}:{username}', home_directory], check=True)
    except FileNotFoundError:
        # Handle the case when 'useradd' command is not available
        # Fallback solution: Create a directory manually and assign appropriate permissions
        home_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'user_data', username)
        subprocess.run(['mkdir', '-p', home_directory], check=True)
        subprocess.run(['chown', f'{username}:{username}', home_directory], check=True)

def register(request):
    if request.method == 'POST':
        # Process the user registration form
        username = request.POST.get('username')
        # ... other registration logic ...

        # Create the Linux user
        create_linux_user(username)

        # ... continue with user registration and other logic ...

    return render(request, 'register.html')