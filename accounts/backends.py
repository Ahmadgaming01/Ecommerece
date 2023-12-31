from django.contrib.auth.backends import ModelBackend , UserModel
from django.contrib.auth.models import User
from django.db.models import Q


class EmailBackend (ModelBackend):
    def authenticate(self, request, username:None, password:None,  **kwargs):
        try:
            user=User.objects.get(
                Q (username__iexact = username) |
                Q (email__iexact = username)
            )
        except User.DoesNotExist:
            pass

        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        
        #return super().authenticate(request, username, password, **kwargs)
