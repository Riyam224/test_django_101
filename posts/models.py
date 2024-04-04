from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Posts(models.Model):
    """Model definition for Posts."""
    title =  models.CharField(_("title"), max_length=50)
    desc =  models.TextField(_("desc"))


    # TODO: Define fields here

    class Meta:
        """Meta definition for Posts."""

        verbose_name = 'Posts'
        verbose_name_plural = 'Postss'

    def __str__(self):
        """Unicode representation of Posts."""
        return str(self.title)
