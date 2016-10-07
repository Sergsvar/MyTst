from django.shortcuts import render
from .forms import AddBd, PostForm


# Create your views here.
def home(request):

    return render(request, 'tst/home.html')

def bd(request):
    form = AddBd(request.POST)
    add = form.save(commit=False)
    add.region = 'Vostok'
    add.country = 'Syria'
    add.value = 23.5
    add.save()
    return render(request, 'tst/parse.html')

def new(request):
    form = PostForm()
    return render(request, 'tst/new.html')
