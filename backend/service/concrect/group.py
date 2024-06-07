from django.contrib.auth.models import Group
from backend.service.helper import paginator

class GroupService:
   
    def findAll(self):
        data = Group.objects.all()
        return data
    
    def findAllPage(self, request):
        data = self.findAll()
        return paginator(request, data)
    
    def findById(self, id):
        return Group.objects.filter(id = id).first()
    
    def findByName(self, name):
        return Group.objects.filter(name = name).first()
    
    def findOrSave(self, data: Group):
        group = self.findByName(data.name)
        if group != None: 
            return group
        return self.save(data)
    
    def save(self, data: Group):
        data.save()
        return data
    
    def update(self, data: Group):
        Group.objects.filter(id = data.id).update(name = data.name)
        return data
    
    def delete(self, id):
        data = self.findById(id)
        data.delete()
        return data    