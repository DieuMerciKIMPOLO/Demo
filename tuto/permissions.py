from rest_framework.permissions import *

#class BasePermission(object):


    #def has_permission(self, request, view):

        #return True

    #def has_object_permission(self, request, view, obj):

        #return True


class IsAdmin(BasePermission):
	"""La permission de  IsAdmin"""

	def has_permission(self, request, view):
		{'error': 'vous n" avez pas le droit d" effectuer cette action'}
		return not request.user.is_superuser==True

		
