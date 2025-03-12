from django.shortcuts import render


def home(request):
    template_name = 'home.html'
    context = {
        'title': 'Nasrullah',
        'umur' : 20,
    }
    return render(request, template_name, context)