"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views # Ajout de la vue créée

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bands/', views.band_list, name='band-list'), # URL vers la vue bands
    path('bands/<int:id>/', views.band_detail, name='band-detail'), # URL pour un groupe précis
    path('bands/add/', views.band_create, name='band-create'), # URL pour ajouter un groupe
    path('bands/<int:id>/update/', views.band_update, name='band-update'), # URL pour modifier un groupe
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'), # URL pour supprimer un groupe

    path('about-us/', views.about, name='about'), # URL vers à propos
    path('contact-us/', views.contact, name='contact'), # URL vers le formulaire de contact

    path('listings/', views.listings, name='listing-list'), # URL vers le listing
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'), # URL pour une annonce précise
    path('listings/add/', views.listing_create, name='listing-create'), # URL pour ajouter une annonce
    path('listings/<int:id>/update/', views.listing_update, name='listing-update'), # URL pour modifier une annonce
    path('listings/<int:id>/delete/', views.listing_delete, name='listing-delete'), # URL pour supprimer une annonce

    path('email-sent/', views.email, name='email-sent') # URL pour  le retour du formulaire de contact
]
