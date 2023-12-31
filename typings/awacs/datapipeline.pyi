"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Data Pipeline"
prefix = "datapipeline"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

ActivatePipeline = Action("ActivatePipeline")
AddTags = Action("AddTags")
CreatePipeline = Action("CreatePipeline")
DeactivatePipeline = Action("DeactivatePipeline")
DeletePipeline = Action("DeletePipeline")
DescribeObjects = Action("DescribeObjects")
DescribePipelines = Action("DescribePipelines")
EvaluateExpression = Action("EvaluateExpression")
GetAccountLimits = Action("GetAccountLimits")
GetPipelineDefinition = Action("GetPipelineDefinition")
ListPipelines = Action("ListPipelines")
PollForTask = Action("PollForTask")
PutAccountLimits = Action("PutAccountLimits")
PutPipelineDefinition = Action("PutPipelineDefinition")
QueryObjects = Action("QueryObjects")
RemoveTags = Action("RemoveTags")
ReportTaskProgress = Action("ReportTaskProgress")
ReportTaskRunnerHeartbeat = Action("ReportTaskRunnerHeartbeat")
SetStatus = Action("SetStatus")
SetTaskStatus = Action("SetTaskStatus")
ValidatePipelineDefinition = Action("ValidatePipelineDefinition")
