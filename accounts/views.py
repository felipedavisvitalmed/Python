from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect


def register_view(request):
     if request.method == 'POST':
            user_form = UserCreationForm(request.POST)
            if user_form.is_valid():
                 user_form.save()
                 return redirect('login')
     else:       
        user_form = UserCreationForm()
    
     return render(request,
                   'register.html',
                   {'user_form': user_form}
                   )

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm(request, data=request.POST) 
            login_form.errors.clear()  # Remove os erros padrão 
            login_form.add_error(None, 'Invalid username or password')
        

    else:
        login_form = AuthenticationForm()    
    return render(request, 
                  'login.html',
                    {'form': login_form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'logout.html')