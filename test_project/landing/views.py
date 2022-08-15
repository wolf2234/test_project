from django.shortcuts import render, HttpResponse
from .forms import SubscribersForm
# Create your views here.


def landing(request):
    name = 'CodingMadved'
    current_day = '09.09.2022'
    form = SubscribersForm(request.POST or None)
    if request.POST and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data.get('name'))
        new_form = form.save()

    return render(request, 'landing/landing.html', locals())


