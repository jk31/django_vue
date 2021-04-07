from rest_framework import permissions


class OnlyOwnerPermission(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		return obj.owner == request.user


class OnlyAdminPermission(permissions.BasePermission):
	# same as rest_framework.permissions.isAdminUser
	def has_permission(self, request, view):
		user = request.user
		return user.is_staff