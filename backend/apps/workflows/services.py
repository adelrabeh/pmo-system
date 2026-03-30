from django.utils import timezone
from .models import WorkflowAction

def approve_workflow_step(instance, approver, comments=""):
    current_step = instance.template.steps.get(step_order=instance.current_step_order)
    WorkflowAction.objects.create(instance=instance, step=current_step, approver=approver, decision="approved", comments=comments, acted_at=timezone.now())
    next_step = instance.template.steps.filter(step_order=instance.current_step_order + 1).first()
    if next_step:
        instance.current_step_order += 1
        instance.overall_status = "in_progress"
    else:
        instance.overall_status = "approved"
    instance.save()
    return instance
