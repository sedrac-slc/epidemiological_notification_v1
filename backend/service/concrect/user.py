from django.contrib.auth.models import User

class UserService:
   
    def findByUsername(self, username):
        return User.objects.filter(username = username).first()
    
    def findOrSave(self, data: User):
        user = self.findByUsername(data.username)
        if user != None: 
            return user
        return self.save(data)
    
    def save(self, data: User):
        data.save()
        return data