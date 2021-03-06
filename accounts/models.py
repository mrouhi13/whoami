from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance=None, **kwargs):
    instance.profile.save()


def upload_to(instance, filename):
    return 'gallery/{}/{}'.format(instance.owner_id, filename)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError('Email is blank.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """
    An abstract class implementing a fully featured User model with
    admin-compliant permissions.

    Email and password are required. Other fields are optional.
    """

    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_('email address'), unique=True, error_messages={
        'unique': 'Email must be unique.'})
    is_suspend = models.BooleanField(_('suspend'), default=False,
                                     help_text=_(
                                         'Designates whether this user should be treated as active. '
                                         'Unselect this instead of deleting accounts.'))

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Profile(models.Model):
    GENDER_NO_BINARY = 'no-binary'
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_CHOICES = (
        (GENDER_NO_BINARY, _('No-binary')),
        (GENDER_MALE, _('Male')),
        (GENDER_FEMALE, _('Female')),
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE,
                                 verbose_name=_('owner'))
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    mobile = models.CharField(_('mobile'), max_length=30, blank=True)
    bio = models.TextField(_('bio'), max_length=500, blank=True)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    gender = models.CharField(_('gender'), max_length=1,
                              choices=GENDER_CHOICES,
                              default=GENDER_NO_BINARY)
    avatar = models.ImageField(_('avatar'), upload_to=upload_to)
