from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'store/index.html')

def contact(request):
    return render(request, 'store/contact.html')