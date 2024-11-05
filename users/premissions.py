from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """ Получение объектов пользователя """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
