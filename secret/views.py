from django.shortcuts import render
from django.contrib import messages
from .models import Secret

# Create your views here.
def index(request):
    return render(request, "secret/index.html")

def create_secret(request):
    # Fetch the secret from the form
    secret = request.POST.get("secret")
    
    # Create a record
    secret = Secret.objects.create(secret=secret)
    messages.success(request, "Secret created successfully!")
    if request.htmx:
        return render(request, "secret/create.html", {"secret": secret})
    return render(request, "secret/index.html", {"secret": secret})

def read_secret(request, uuid):
    # Fetch the record
    secret = Secret.objects.get(uuid=uuid)
    
    # Render the response
    response = render(request, "secret/read.html", {"secret": secret})
    
    # Delete the record
    secret.delete()
    return response
