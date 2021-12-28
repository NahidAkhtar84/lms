from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    #for creating user
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('User Name is required')

        user = self.model(
            username=self.normalize_email(username),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # for creating super user
    def create_superuser(self, username, password, **args):
        user = self.create_user(
            username=self.normalize_email(username),
            password = password
        )
        user.email=args["email"]
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user