from django.shortcuts import render
from django.views.generic import View
from django.contrib import messages

from lesson15_1.forms import FirstForm


def index(request):
    return render(request, 'lesson15_1/index.html')


class FirstView(View):
    def get(self, request):
        form = FirstForm()
        return render(request, 'lesson15_1/index.html', {'form':form})

    def post(self, request):
        form = FirstForm(request.POST)
        if form.is_valid():
            messages.success(request, form.cleaned_data['message'])
        else:
            messages.error(request, 'Validation failed')
        return render(request, 'lesson15_1/index.html', {'form':form})

