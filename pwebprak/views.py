from django.shortcuts import render


def home(request):
    template_name = 'halaman/base.html'
    context = {
        'title': 'Nasrullah',
        'umur' : 20,
    }
    return render(request, template_name, context)

def about(request):
    template_name = "about.html"
    context = {
        'title' : 'Selamat datang di halaman about',
        'umur' : 20,
    }
    return render(request, template_name, context)