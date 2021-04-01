from django.shortcuts import render, redirect

from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.


    #{"nombre de variable": de servicios}
def contacto(request):
    #esto es una instancia 
    formulario_contacto=FormularioContacto()

    #para la peticion post
    if request.method=="POST":  #si se hizo post enviar 
         formulario_contacto=FormularioContacto(data=request.POST)
         #carga en el formulario_contacto la informacion que se envia de post
         if formulario_contacto.is_valid():  #si el formulario_contacto es valido
             nombre=request.POST.get("nombre")
             #que lo guarde en una variable nombre (lo que esta en nombre)
             email=request.POST.get("email")
             contenido=request.POST.get("contenido")


             #colocar sequence/ el mensaje que recibes
             #.format(nombre,email,contenido), esto es un constructor
             email= EmailMessage("Mensaje desde App Django",
             "El usuario con nombre {} con la dirección {} escribe lo siguiente:\n\n {}".format(nombre,email,contenido),
             "",["benjarowe90@gmail.com"],reply_to=[email])
             

             try:
                 email.send()
                 return redirect("/contacto/?valido")
             except:
                 return redirect("/contacto/?novalido")



    return  render(request, "portafolio/contacto.html", {'miFormulario':formulario_contacto})