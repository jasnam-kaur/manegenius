from django.shortcuts import render

def home(request):
    # This function looks for 'index.html' inside your templates folder
    return render(request, 'index.html')
# accounts/views.py

# ... existing imports and home view ...

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def events(request):
    return render(request, 'events.html')
def management_sapiens(request):
    return render(request, 'managementSapeins.html')

def select(request):
    return render(request, 'select.html')

def madteam(request):
    return render(request, 'madteam.html')

def contact(request):
    return render(request, 'contact.html')
def auction(request):
    return render(request, 'auction.html')

def product_remix(request):
    return render(request, 'productremix.html')

def thinksink(request):
    return render(request, 'thinksink.html')

def brandplay(request):
    return render(request, 'brandplay.html')

def madmoments(request):
    return render(request, 'madmoments.html')

def treasuretrack(request):
    return render(request, 'treasuretrack.html')
def auction_register(request):
    return render(request, 'auctionregister.html')
def brandplay_register(request):
    return render(request, 'brandplayregister.html')

def madmoments_register(request):
    return render(request, 'madmomentsregister.html')
def thinksink_register(request):
    return render(request, 'thinksinkregister.html')

def treasuretrack_register(request):
    return render(request, 'treasuretrackregister.html')
def productremix_register(request):
    return render(request, 'productremixregister.html')
def drishya(request):
    return render(request, 'drishya.html')

def fintellect(request):
    return render(request, 'fintellect.html')

def marquest(request):
    return render(request, 'marquest.html')

def unnati(request):
    return render(request, 'unnati.html')