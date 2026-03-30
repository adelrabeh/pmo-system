from django.db import models
from django.utils import timezone
from apps.users.models import User
class TimestampedModel(models.Model):
    created_at=models.DateTimeField(default=timezone.now)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta: abstract=True
class WorkflowTemplate(TimestampedModel):
    name_ar=models.CharField(max_length=200, unique=True)
    applies_to=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
class WorkflowStep(TimestampedModel):
    template=models.ForeignKey(WorkflowTemplate,on_delete=models.CASCADE,related_name="steps")
    step_order=models.PositiveIntegerField()
    step_name_ar=models.CharField(max_length=200)
    approver_role_name=models.CharField(max_length=150)
    sla_hours=models.PositiveIntegerField(default=48)
    is_mandatory=models.BooleanField(default=True)
class WorkflowInstance(TimestampedModel):
    template=models.ForeignKey(WorkflowTemplate,on_delete=models.PROTECT,related_name="instances")
    entity_type=models.CharField(max_length=100)
    entity_id=models.BigIntegerField()
    current_step_order=models.PositiveIntegerField(default=1)
    overall_status=models.CharField(max_length=50, default="pending")
    initiated_by=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="initiated_workflows")
class WorkflowAction(TimestampedModel):
    instance=models.ForeignKey(WorkflowInstance,on_delete=models.CASCADE,related_name="actions")
    step=models.ForeignKey(WorkflowStep,on_delete=models.PROTECT,related_name="actions")
    approver=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name="workflow_actions")
    decision=models.CharField(max_length=50, default="pending")
    comments=models.TextField(blank=True)
    acted_at=models.DateTimeField(null=True,blank=True)
