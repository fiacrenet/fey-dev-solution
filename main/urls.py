from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apropos', views.apropos, name='apropos'),
    path('contact', views.contact, name='contact'),
    path('creationSiteWeb', views.creationSiteWeb, name='creationSiteWeb'),
    path('referencement', views.referencement, name='referencement'),
    path('maintenance', views.maintenance, name='maintenance'),
]
