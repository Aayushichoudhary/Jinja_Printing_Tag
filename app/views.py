from django.shortcuts import render

# Create your views here.

def data_render(request):
    data='This data is our assumption'
    d={'aayushi':data, 'age':'Aayushi'}
    return render(request,'data_render.html',context=d)