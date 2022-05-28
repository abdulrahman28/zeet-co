from django.shortcuts import render 
from django.http import HttpResponse
from .models import intel


# Create your views here.

def index(request):

    db = intel.objects.all()

    context = {
        'intels' : db,
}
    return render(request,'index.html', context)


def signin(request):


    return render(request,'signin.html')



def sum(request):

    a = request.POST['first']
    b = request.POST['second']

    if a == '' or b == '':
        context = {'res':'No Data Entered!!!'}
        return render(request, 'sum.html', context)  

    else:
        a = float(a)
        b = float(b)       
        c = 'The result is ' + str(a + b)
        context = {
            'res':c
            }
        return render(request, 'sum.html', context)



      

