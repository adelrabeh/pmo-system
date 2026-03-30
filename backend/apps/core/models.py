from django.db import models
class Department(models.Model):
    name_ar = models.CharField(max_length=200, unique=True)
    def __str__(self): return self.name_ar
class ProjectStatus(models.Model):
    name_ar = models.CharField(max_length=100, unique=True)
    color_hex = models.CharField(max_length=10, blank=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta: ordering=["sort_order","id"]
    def __str__(self): return self.name_ar
class ProjectPhase(models.Model):
    name_ar = models.CharField(max_length=100, unique=True)
    sort_order = models.PositiveIntegerField(default=0)
    class Meta: ordering=["sort_order","id"]
    def __str__(self): return self.name_ar
class ProjectPriority(models.Model):
    name_ar = models.CharField(max_length=100, unique=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    def __str__(self): return self.name_ar
class SeverityLevel(models.Model):
    name_ar = models.CharField(max_length=100, unique=True)
    weight = models.PositiveIntegerField(default=1)
class ProbabilityLevel(models.Model):
    name_ar = models.CharField(max_length=100, unique=True)
    weight = models.PositiveIntegerField(default=1)
class ImpactLevel(models.Model):
    name_ar = models.CharField(max_length=100, unique=True)
    weight = models.PositiveIntegerField(default=1)
class ChangeDecisionStatus(models.Model):
    name_ar = models.CharField(max_length=100, unique=True)
