from django.conf.urls import url
from tuto import views

#router = routers.DefaultRouter()
#router.register(r'utilisateurs', views.ProfilutilisateurViewSet.as_view())
#router.register(r'messages', views.MessagesViewSet)
#router.register(r'connexion', views.ConnexionViewSet)
#router.register(r'role_utilisateur', views.RoleUtilisateurViewSet)
#router.register(r'citations', views.CitationsViewSet)

urlpatterns = [
    url(r'^utilisateurs/ajouter/$', views.ProfilutilisateurViewAdd.as_view()),
    url(r'^utilisateurs/liste/$', views.ProfilutilisateurViewList.as_view()),
    #url(r'^utilisateurs/(?P<is_active>[a-zA-Z])/liste/$', views.ProfilutilisateurViewList.as_view()),
    #---
    url(r'^messages/ajouter/$', views.MessagesViewAdd.as_view()),
    url(r'^messages/liste/$', views.MessagesViewList.as_view()),
    #--
    url(r'^connexions/ajouter/$', views.ConnexionViewAdd.as_view()),
    url(r'^connexions/liste/$', views.ConnexionViewList.as_view()),
    #--
    url(r'^citations/ajouter/$', views.CitationViewAdd.as_view()),
    url(r'^citations/liste/$', views.CitationViewList.as_view()),
    #--
    url(r'^role_utilisateurs/ajouter/$', views.RoleUtilisateurViewAdd.as_view()),
    url(r'^role_utilisateurs/liste/$', views.RoleUtilisateurViewList.as_view()),

    #url(r'^messages/$', views.MessagesViewSet.as_view()),
    #url(r'^connexion/$', views.ProfilutilisateurViewSet.as_view()),
    #url(r'^utilisateurs/$', views.ProfilutilisateurViewSet.as_view()),
    #url(r'^utilisateurs/$', views.ProfilutilisateurViewSet.as_view()),

]