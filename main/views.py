from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'application' : 'Toup Up',
        'name': 'Dicky Bayu Sadewo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)