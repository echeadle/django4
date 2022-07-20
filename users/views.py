from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.

def register(request):
    form = NewUserForm()
    context={
        'form':form,
    }
    return render(request, 'users/register.html', context)

