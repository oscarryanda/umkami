from django.shortcuts import render

def home_view(request):
    context = {
        'app_name': 'UMKaMi',
        'student_name': 'Oscar Ryanda Putra',
        'student_class': 'PBP F',
    }
    return render(request, 'main/home.html', context)
