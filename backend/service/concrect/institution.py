from backend.entities.concrect.institution import Institution
from backend.service.helper import paginator

class InstitutionService:
    
    def findAllPage(self, request):
        data = Institution.objects.filter(deleted_at__isnull=True, deleted_by__isnull=True)
        return paginator(request, data)