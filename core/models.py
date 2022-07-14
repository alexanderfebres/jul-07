from django.db import models

from django.contrib.auth.models import User
from crum import get_current_user


class Project(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Title",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Description",
    )
    url = models.URLField(
        verbose_name="Url",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="+",
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="+",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Project"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(Project, self).save(*args, **kwargs)

    @property
    def get_projects_created_by_super_users(self):
        return Project.objects.filter(created_by__is_superuser=True)
