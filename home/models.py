# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenoms = models.CharField(max_length=255, null=True, blank=True)
    date_naissance = models.DateTimeField(blank=True, null=True, default=timezone.now)
    lieu_naissance = models.CharField(max_length=255, null=True, blank=True)
    photo = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Experience(models.Model):

    #__Experience_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    entreprise = models.CharField(max_length=255, null=True, blank=True)
    fonction = models.CharField(max_length=255, null=True, blank=True)

    #__Experience_FIELDS__END

    class Meta:
        verbose_name        = _("Experience")
        verbose_name_plural = _("Experience")


class Education(models.Model):

    #__Education_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    annee = models.DateTimeField(blank=True, null=True, default=timezone.now)
    intitule = models.CharField(max_length=255, null=True, blank=True)

    #__Education_FIELDS__END

    class Meta:
        verbose_name        = _("Education")
        verbose_name_plural = _("Education")


class Profil(models.Model):

    #__Profil_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Profil_FIELDS__END

    class Meta:
        verbose_name        = _("Profil")
        verbose_name_plural = _("Profil")


class Loisirs(models.Model):

    #__Loisirs_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    niveau = models.IntegerField(null=True, blank=True)

    #__Loisirs_FIELDS__END

    class Meta:
        verbose_name        = _("Loisirs")
        verbose_name_plural = _("Loisirs")


class Contact(models.Model):

    #__Contact_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)

    #__Contact_FIELDS__END

    class Meta:
        verbose_name        = _("Contact")
        verbose_name_plural = _("Contact")


class Competance(models.Model):

    #__Competance_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    niveau = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Competance_FIELDS__END

    class Meta:
        verbose_name        = _("Competance")
        verbose_name_plural = _("Competance")


class Project(models.Model):

    #__Project_FIELDS__
    id = models.IntegerField(null=True, blank=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    lien = models.CharField(max_length=255, null=True, blank=True)
    date_debut = models.DateTimeField(blank=True, null=True, default=timezone.now)
    date_fin = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Project_FIELDS__END

    class Meta:
        verbose_name        = _("Project")
        verbose_name_plural = _("Project")


class Avis(models.Model):

    #__Avis_FIELDS__
    nom = models.CharField(max_length=255, null=True, blank=True)
    prenoms = models.CharField(max_length=255, null=True, blank=True)
    date_naissance = models.DateTimeField(blank=True, null=True, default=timezone.now)
    ville = models.CharField(max_length=255, null=True, blank=True)
    contact = models.CharField(max_length=255, null=True, blank=True)
    pays = models.CharField(max_length=255, null=True, blank=True)

    #__Avis_FIELDS__END

    class Meta:
        verbose_name        = _("Avis")
        verbose_name_plural = _("Avis")



#__MODELS__END
