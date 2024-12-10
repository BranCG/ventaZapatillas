from rest_framework.permissions import BasePermission

class IsBrandon(BasePermission):
    """
    Permite el acceso solo al usuario 'brandon'.
    """

    def has_permission(self, request, view):
        # Verifica si el usuario está autenticado y si su nombre de usuario es 'brandon'
        return request.user.is_authenticated and request.user.username == "brandon"
