from django.db import models
from django.utils.translation import gettext as _


class Link(models.Model):
    full_link = models.CharField(_("Link"), max_length=255)
    short_link = models.CharField(_("Short Link"), max_length=255)    
    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.full_link

    #def get_absolute_url(self):
    #    return reverse("_detail", kwargs={"pk": self.pk})