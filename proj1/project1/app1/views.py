from django.shortcuts import render
from . models import Place
from . models import team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'results':obj})

def demo1(request):
    pics=team.objects.all()
    return render(request,"index.html",{'pic':pics})
#def addition(request):
#    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
  #  add=x+y
#    sub=x-y
 #   mul=x*y
 #   div=x/y

 #   return render(request, "result.html", {'result': {'add': add, 'sub': sub, 'mul': mul, 'div': div}})


