from django.contrib.auth.models import Group, Permission
from backend.service.helper import paginator

class GroupService:
   
    def list(self):
        return Group.objects.all()
    
    def findAllPage(self, request):
        return paginator(request, self.list())
    
    def findById(self, id):
        return Group.objects.filter(id = id).first()
    
    def findByName(self, name):
        return Group.objects.filter(name = name).first()
    
    def findOrSave(self, data: Group):
        group = self.findByName(data.name)
        if group != None: 
            return group
        return self.save(data)

    def findInId(self,groupIds):
        return Group.objects.filter(id__in=groupIds).all()

    def findNotInPermission(self, permission_id):
        permission = Permission.objects.get(id=permission_id)
        permission_group_ids = permission.group_set.values_list('id', flat=True)
        groups_not_in_permission = Group.objects.exclude(id__in=permission_group_ids)
        return groups_not_in_permission   

    def save(self, data: Group):
        data.save()
        return data

    def update(self, data: Group):
        Group.objects.filter(id = data.id).update(name = data.name)
        return data