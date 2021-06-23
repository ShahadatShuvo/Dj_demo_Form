from django.shortcuts import render
from .forms import AuthorForm
# Create your views here.


def index(request):
    form = AuthorForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)