"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Amplify"
prefix = "amplify"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

CreateApp = Action("CreateApp")
CreateBackendEnvironment = Action("CreateBackendEnvironment")
CreateBranch = Action("CreateBranch")
CreateDeployment = Action("CreateDeployment")
CreateDomainAssociation = Action("CreateDomainAssociation")
CreateWebHook = Action("CreateWebHook")
DeleteApp = Action("DeleteApp")
DeleteBackendEnvironment = Action("DeleteBackendEnvironment")
DeleteBranch = Action("DeleteBranch")
DeleteDomainAssociation = Action("DeleteDomainAssociation")
DeleteJob = Action("DeleteJob")
DeleteWebHook = Action("DeleteWebHook")
GenerateAccessLogs = Action("GenerateAccessLogs")
GetApp = Action("GetApp")
GetArtifactUrl = Action("GetArtifactUrl")
GetBackendEnvironment = Action("GetBackendEnvironment")
GetBranch = Action("GetBranch")
GetDomainAssociation = Action("GetDomainAssociation")
GetJob = Action("GetJob")
GetWebHook = Action("GetWebHook")
ListApps = Action("ListApps")
ListArtifacts = Action("ListArtifacts")
ListBackendEnvironments = Action("ListBackendEnvironments")
ListBranches = Action("ListBranches")
ListDomainAssociations = Action("ListDomainAssociations")
ListJobs = Action("ListJobs")
ListWebHooks = Action("ListWebHooks")
StartDeployment = Action("StartDeployment")
StartJob = Action("StartJob")
StopJob = Action("StopJob")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")
UpdateApp = Action("UpdateApp")
UpdateBranch = Action("UpdateBranch")
UpdateDomainAssociation = Action("UpdateDomainAssociation")
UpdateWebHook = Action("UpdateWebHook")
