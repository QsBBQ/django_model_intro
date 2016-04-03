from django.test import TestCase
from ModelTest_app.models import Contact

# Create your tests here.

def get_contacts(request):
    return render(request, "ModelTest/home.html",
                  {'contact_list': Contact.objects.all()})
