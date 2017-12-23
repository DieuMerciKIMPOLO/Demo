from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import *
from rest_framework import generics
from rest_framework import viewsets
from tuto.serializer import *
from tuto.permissions import *
from tuto.throttling import *
from tuto.models import *


class ProfilutilisateurViewAdd(generics.CreateAPIView):
    """
        Creation d'un utilisateur avec un modele personnalisee
    """
    #permission_classes = (AllowAny,)
    queryset = Profilutilisateur.objects.all()
    serializer_class = ProfilutilisateurSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProfilutilisateurViewList(generics.ListAPIView):
    """
        Liste  des utilisateurs du modele Profilutilisateur
    """
    #permission_classes = (AllowAny,)
    queryset = Profilutilisateur.objects.all()
    serializer_class = ProfilutilisateurSerializer
    throttle_scope = 'anon'

    #lookup_field = 'is_active'


    #def list(self, request, **kwargs):
    #    queryset = self.queryset.filter(is_active=kwargs["is_active"])
    #    serializer = self.serializer_class(queryset, many=True)
    #    return Response(serializer.data)


#----------------------------------------------------------------------------------------------------------------------------------------
        

class RoleUtilisateurViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = RoleUtilisateur.objects.all()
    serializer_class = RoleUtilisateurSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class RoleUtilisateurViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = RoleUtilisateur.objects.all()
    serializer_class = RoleUtilisateurSerializer
   

#----------------------------------------------------------------------------------------------------------

class CitationViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Citations.objects.all()
    serializer_class = CitationsSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CitationViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = Citations.objects.all()
    serializer_class = CitationsSerializer


#-----------------------------------------------------------------------------------------------------------
class ConnexionViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    #permission_classes = (AllowAny,)
    queryset = Connexion.objects.all()
    serializer_class = ConnexionSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ConnexionViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = Connexion.objects.all()
    serializer_class = ConnexionSerializer

#----------------------------------------------------------------------------------------------------------

class MessagesViewAdd(generics.CreateAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            data_errors = {}
            data_message = str('')
            for P, M in serializer.errors.items():
                data_message += P + ": " + M[0].replace(".", '')
            data_errors['error'] = data_message
            return Response(data_errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessagesViewList(generics.ListAPIView):
    """
        API endpoint that allows groups to be viewed or edited.
    """
    permission_classes = (AllowAny,)
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

 