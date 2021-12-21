from django.shortcuts import render
from backend.models import Contact

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def form_view(request):
    if request.method == 'GET':
        return render(request, 'form.html')
    elif request.method == 'POST':
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        Contact.objects.create(name = name, phone_number = phone_number)
        return render(request, 'succes.html')

def contact_list_view(request):
    contact = Contact.objects.all()
    context = {
        'contact': contact
    }
    return render(request, 'contactList.html', context)
