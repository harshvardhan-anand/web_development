from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage/homepage.html')
    
def about(request):
    return render(request, 'app/about.html')

def pricing(request):
    return render(request, 'app/pricing.html')