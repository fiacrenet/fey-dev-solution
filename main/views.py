from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def apropos(request):
    return render(request, 'a-propos.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:  # Vérifie que tous les champs sont remplis
            contact = Contact(name=name, email=email, message=message)
            contact.save()  # Sauvegarde dans la base de données
            messages.success(request, 'Merci pour votre message. Nous vous répondrons bientôt.')
            return redirect('contact')  # Redirection après succès
        else:
            messages.error(request, 'Veuillez remplir tous les champs.')  # Message d'erreur si champs manquants
    
    return render(request, 'contact.html')  # Affiche le formulaire

def creationSiteWeb(request): 
    return render(request, 'creation-de-site-web.html')

    