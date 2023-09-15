from django.shortcuts import render

from .models import Placedetails, actors


# Create your views here.
def demo(request):
    obj=Placedetails.objects.all()
    obj1=actors.objects.all()
    return render(request, "index.html", {'result':obj, 'result1':obj1})


