from django.contrib.auth.models import Permission
from backend.service.helper import paginator
from django.db.models import Q

class PermissionService:

    def findAll(self):
        data = Permission.objects.select_related('content_type').filter(content_type__app_label="backend")     
        return data

    def findAllPage(self, request):
        data = self.findAll()
        return paginator(request, data)