from django.contrib.auth.models import Permission, Group
from backend.service.helper import paginator
from django.db.models import Q

class PermissionService:

    def list(self):
        return Permission.objects.select_related('content_type').filter(content_type__app_label="backend")
    
    def findAll(self):     
        return self.list().all()
    
    def findById(self,id):
        return Permission.objects.filter(id = id).first()
    
    def findInId(self,permissionIds):
        return Permission.objects.filter(id__in=permissionIds).all()

    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findNotInGroup(self, group_id):
        group = Group.objects.get(id=group_id)
        group_permission_ids = group.permissions.values_list('id', flat=True)
        permissions_not_in_group = Permission.objects.select_related('content_type').filter(content_type__app_label="backend").exclude(id__in=group_permission_ids)
        return permissions_not_in_group    