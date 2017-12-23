#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tuto.models import *


class ProfilutilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilutilisateur
        exclude = ('is_superuser','is_staff','is_active')

class ProfilutilisateurListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profilutilisateur
        fields = '__all__'

class RoleUtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleUtilisateur
        fields = '__all__'



class CitationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citations
        fields = '__all__'


class ConnexionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connexion
        fields = '__all__'


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = '__all__'