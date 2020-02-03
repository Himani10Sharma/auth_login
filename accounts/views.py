from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registration/login.html')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login(request):
    if request.method == 'POST':
        return render(request,'home.html')
    else:
        pass
    return render(request, 'login.html')


def logout(request):
    return HttpResponse("i m ok")