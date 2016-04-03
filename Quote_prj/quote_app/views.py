from django.shortcuts import render
from quote_app.models import Quotes

# Create your views here.

def get_quotes(request):
    return render(request, "quote/home.html",
                 {'quote_list': Quotes.objects.all()})
