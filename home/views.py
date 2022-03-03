from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Initial view to render index.html
    """

    return render(request, 'home/index.html')
