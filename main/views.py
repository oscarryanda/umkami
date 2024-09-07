from django.shortcuts import render

def show_main(request):
    context = {
        'app' : 'Toko Ungu',
        'name': 'Jeremia Rangga',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)