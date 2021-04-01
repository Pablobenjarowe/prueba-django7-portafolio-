from django.shortcuts import render, HttpResponse

#formulario y se agrego redirect



#---------------------------------------------------------index

def home(request):
    return  render(request, "portafolio/index.html")

#--------------------------------------------------------formulario contacto
    #{"nombre de variable": de servicios}
