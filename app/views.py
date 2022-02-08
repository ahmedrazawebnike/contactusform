from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import CONTACT_MODAL
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        if (name != '' and email != '' and msg != ''):                
            CONTACT_MODAL(
                name= name,
                email= email,
                msg= msg,
            ).save()
            messages.success(request, f'Mr "{name}"! your query has been submited successfully.')
        else:
            messages.success(request, 'Make sure that all fields are required')
        return redirect('/')