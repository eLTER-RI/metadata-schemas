import dataclasses
from typing import Optional

from oarepo_workflows import WorkflowTransitions

@dataclasses.dataclass
class ExternalWorkflowTransitions(WorkflowTransitions):
    canceled: Optional[str] = None
