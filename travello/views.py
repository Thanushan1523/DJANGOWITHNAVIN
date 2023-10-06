from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name= 'canada'
    dest1.price=800
    dest1.image='destination_1.jpg'

    dest2 = Destination()
    dest2.name= 'ontario'
    dest2.price=1000
    dest2.image='destination_2.jpg'

    dest3 = Destination()
    dest3.name= 'toronto'
    dest3.price=2000
    dest3.image='destination_1.jpg'

    dests=[dest1,dest2,dest3]

    
    return render(request, 'index.html',{'dests' :dests})
