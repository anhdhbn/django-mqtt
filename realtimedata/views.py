from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def room(request, device):
    return render(request, 'room.html', {
        'device': device
    })