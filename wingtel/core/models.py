from datetime import datetime

from django.utils import timezone
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin, Permission, Group)
from model_utils import Choices


class TimeStampedQuerySet(models.query.QuerySet):
    """
    Used to override the default update and bulk_create methods that
    that will handle updating the modified_date and/or created_date
    """

    def bulk_create(self, *args, **kwargs):
        now = timezone.now()
        for obj in args[0]:
            obj.created_date = now
            obj.modified_date = now
        return super(TimeStampedQuerySet, self).bulk_create(*args, **kwargs)

    def update(self, *args, **kwargs):
        if 'modified_date' not in kwargs:
            now = timezone.now()
            kwargs['modified_date'] = now
        return super(TimeStampedQuerySet, self).update(*args, **kwargs)


class TimeStamped(models.Model):
    """
    Abstract Model that provides timestamping for an object and
    enforces the updating of the timestamps regardless of user
    interaction with the model. Do not need to specify the created_date
    or modified_date fields when creating objects that inherit from
    this.
    """
    created_date = models.DateTimeField(editable=False, null=False,
                                        blank=False)
    modified_date = models.DateTimeField(null=False, blank=False)

    def save(self, *args, **kwargs):
        """
        Overwrite save method to enforce the update of modified_date
        and correct creation of created_date. Necessary due to
        issues with Django's auto_now and auto_now_add arguments
        to datetime fields
        """
        now = timezone.now()
        if self.id is None:
            self.created_date = now
        self.modified_date = now
        if 'update_fields' in kwargs:
            if 'modified_date' not in kwargs['update_fields']:
                kwargs['update_fields'].append('modified_date')
        return super(TimeStamped, self).save(*args, **kwargs)

    objects = TimeStampedQuerySet.as_manager()

    class Meta:
        abstract = True


class SoftDeletableQuerySet(models.query.QuerySet):
    """
    Used to override the default delete method on a queryset and
    provide some other convenience methods.
    """

    def delete(self):
        """
        Override default delete method to set the deleted field to true
        rather than actual delete the objects in a queryset
        """
        return super(SoftDeletableQuerySet, self).update(deleted=True)

    def hard_delete(self):
        """
        Used to actually delete the queryset
        """
        return super(SoftDeletableQuerySet, self).delete()

    def deleted(self):
        """
        Return objects that are deleted
        """
        return self.filter(deleted=True)

    def not_deleted(self):
        """
        Return objects that are not deleted
        """
        return self.filter(deleted=False)


class SoftDeletable(models.Model):
    """
    Replaces traditional deletion concept with a boolean field that is
    set true on deletion
    """
    deleted = models.BooleanField(default=False)

    objects = SoftDeletableQuerySet.as_manager()

    class Meta:
        abstract = True

    def delete(self):
        """
        override the default delete method with a function that sets
        deleted equal to True rather than actually deleting the object
        """
        self.deleted = True
        self.save()

    def hard_delete(self):
        """
        allow deletion if absolutely needed
        """
        super(SoftDeletable, self).delete()


class TelecommunicationCompany(TimeStamped, SoftDeletable):
    STATUS = Choices(
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    status = models.CharField(max_length=10, choices=STATUS, default=STATUS.active)
    name = models.CharField(max_length=50)
    website = models.CharField(max_length=50, blank=True)
    one_kilobyte_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.001)
    one_second_price = models.DecimalField(decimal_places=4, max_digits=20, default=0.001)
    network_type = models.CharField(max_length=5, blank=True)


class CustomUser(AbstractBaseUser):

    email = models.EmailField(verbose_name='email address', max_length=255)
    first_name = models.TextField(blank=True, null=True, db_index=True)
    last_name = models.TextField(blank=True, null=True, db_index=True)

    is_active = models.BooleanField(default=True)

    # Only the system user have the below set to True
    is_admin = models.BooleanField(default=False)
