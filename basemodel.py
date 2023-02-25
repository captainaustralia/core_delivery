from typing import Any, Final, Optional
from uuid import uuid4

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import QuerySet
from django.utils import timezone


class OverloadQueryset(QuerySet):
    ...


class OverloadBaseManager(models.Manager):
    def get_queryset(self) -> QuerySet:
        qs = OverloadQueryset(self.model)
        return qs.filter(deleted=False)


class BaseModel(models.Model):
    """
    Notice: \n
    The base model, which will replace the standard models.Model, will add: \n
    - uuid instead of id
    - change time tracking
    - creation time tracking
    - add a deleted field to exclude instances from the queryset
    ALL MODEL MUST BE INHERITED FROM THIS BASEMODEL
    """

    uuid = models.UUIDField(
        default=uuid4,
        editable=False,
        unique=True,
        db_index=True,
        primary_key=True
    )
    date_modified = models.DateTimeField()
    date_created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    objects = OverloadBaseManager()

    def delete(self, using: Optional[bool] = None, keep_parents: bool = False) -> None:
        """
        Don't delete , hide better..
        """
        self.deleted = True
        self.save(update_fields=["deleted"])

    def save(
            self,
            force_insert: bool = False,
            force_update: bool = False,
            using: Optional[bool] = None,
            update_fields: Optional[list[str]] = None,
    ) -> None:
        """
        Save overload , for change time modified
        """
        self.date_modified = timezone.now()
        super().save()

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager, OverloadBaseManager):
    """
    Overload user manager
    """

    use_in_migrations: Final = True

    def _create_user(
            self,
            email: str,
            password: str,
            is_staff: bool,
            is_superuser: bool,
            is_active: bool,
            **extra: dict
    ) -> "BaseUser":
        """
        Overload BaseUserManager ,for better control
        over custom model and easy extensibility
        :param email: str
        :param password: str
        :param is_staff: bool
        :param is_superuser: bool
        :param is_active: bool
        :param extra: dict
        :return: CustomBaseUser
        """
        email = self.normalize_email(email)
        user: "BaseUser" = self.model(
            email=email,
            password=make_password(password),
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra
        )
        user.save()
        return user

    def create_user(
            self,
            email: str,
            password: str,
            is_staff: bool = False,
            is_superuser: bool = False,
            is_active: bool = False,
            **extra: Any
    ) -> "BaseUser":
        """
        Base method for creation User objects use implementation private method,
        can be extended in future
        :param email: str
        :param password: str
        :param is_staff: bool
        :param is_superuser: bool
        :param is_active: bool
        :param extra:
        :return:
        """
        return self._create_user(
            email, password, is_staff, is_superuser, is_active, **extra
        )

    def create_superuser(self, email: str, password: str) -> None:
        self._create_user(
            email, password, is_staff=True, is_superuser=True, is_active=True
        )


class BaseUser(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    Base User model
    """

    email = models.CharField(unique=True, max_length=40, db_index=True)
    date_register = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    REQUIRED_FIELDS: list[str] = []
    USERNAME_FIELD = "email"

    def __str__(self) -> str:
        return str(self.email)

    class Meta:
        abstract = True
