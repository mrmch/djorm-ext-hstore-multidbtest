
from django.db import models

from django_extensions.db.fields.json import JSONField
from djorm_hstore.fields import DictionaryField
from djorm_hstore.models import HStoreManager

from django.contrib.auth.models import User

class Customer(models.Model):
    # Use HStore model manager
    objects = HStoreManager()

    user = models.ForeignKey(User, related_name='customers')

    email = models.EmailField(db_index=True)
    data = DictionaryField(db_index=True)

    class Meta:
        unique_together = ('user', 'email')

    def __unicode__(self):
        return u'%s' % self.email

    def update_data(self, new_data):
        new_customer_data = self.data.copy().update(new_data)
        if not new_customer_data == self.data:
            self.data.update(new_data)
            self.save()

