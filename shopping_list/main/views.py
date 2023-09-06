from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Daffa Al Fathan Zaki',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)