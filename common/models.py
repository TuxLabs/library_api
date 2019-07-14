from django.db import models
from django.utils import timezone
from django.db.models import Manager as GeoManager
from django.contrib.auth.models import User
import base62


# Create your models here.
class _BaseAbstract(models.Model):
    id62 = models.CharField(max_length=100, db_index=True, blank=True, null=True)
    
    created_at = models.DateTimeField(db_index=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, 
                                related_name="%(app_label)s_%(class)s_created_by")

    deleted_at = models.DateTimeField(blank=True, null=True)
    deleted_by = models.ForeignKey(User, db_index=True, blank=True, 
                                null=True, on_delete=models.CASCADE,
                                related_name="%(app_label)s_%(class)s_deleted_by")
    
    objects = GeoManager() 
    
    def save(self, *args, **kwargs):
        now = timezone.now()

        # create first time record
        if self.created_at is None:
            self.created_at = now

        # always update
        self.updated_at = now

        # save the first time record
        instance = super(_BaseAbstract, self).save(*args, **kwargs)

        # generate id62
        if self.id and not self.id62:
            self.id62 = base62.encode(self.id)
            kwargs['force_insert'] =  False
            instance = super(_BaseAbstract, self).save(*args, **kwargs)
        
        return instance
    
    def delete(self, user=None, *args, **kwargs):
        if not user:
            user = self.created_by

        self.deleted_by = user
        self.deleted_at = timezone.now()

        # save it if there's a deleter
        return super(_BaseAbstract, self).save(*args, **kwargs)
    
    class Meta:
        abstract = True

class BaseModelGeneric(_BaseAbstract):
    created_by = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE,
                                related_name="%(app_label)s_%(class)s_created_by")

    class Meta:
        abstract = True