"""
This type stub file was generated by pyright.
"""

from . import AWSObject, AWSProperty

VALID_IMAGE_PULL_CREDENTIALS = ...
VALID_CREDENTIAL_PROVIDERS = ...
VALID_WEBHOOKFILTER_TYPES = ...
VALID_PROJECTFILESYSTEMLOCATION_TYPE = ...

def validate_image_pull_credentials(image_pull_credentials):
    """Validate ImagePullCredentialsType for Project"""
    ...

def validate_credentials_provider(credential_provider):
    """Validate CredentialProvider for Project's RegistryCredential"""
    ...

def validate_webhookfilter_type(webhookfilter_type):
    """Validate WebHookFilter type property for a Project"""
    ...

def validate_projectfilesystemlocation_type(projectfilesystemlocation_type):
    """Validate ProjectFileSystemLocation type property"""
    ...

class SourceAuth(AWSProperty):
    props = ...
    def validate(self): ...

class Artifacts(AWSProperty):
    props = ...
    def validate(self): ...

class EnvironmentVariable(AWSProperty):
    props = ...
    def validate(self): ...

class RegistryCredential(AWSProperty):
    props = ...

class Environment(AWSProperty):
    props = ...
    def validate(self): ...

class BatchRestrictions(AWSProperty):
    props = ...

class ProjectBuildBatchConfig(AWSProperty):
    props = ...

class ProjectCache(AWSProperty):
    props = ...
    def validate(self): ...

class BuildStatusConfig(AWSProperty):
    props = ...

class GitSubmodulesConfig(AWSProperty):
    props = ...

class Source(AWSProperty):
    props = ...
    def validate(self): ...

class VpcConfig(AWSProperty):
    props = ...

class WebhookFilter(AWSProperty):
    props = ...

class ProjectTriggers(AWSProperty):
    props = ...
    def validate(self):
        """FilterGroups, if set, needs to be a list of a list of
        WebhookFilters
        """
        ...

def validate_status(status):
    """Validate status
    :param status: The Status of CloudWatchLogs or S3Logs
    :return: The provided value if valid
    """
    ...

class CloudWatchLogs(AWSProperty):
    props = ...

class S3Logs(AWSProperty):
    props = ...

class LogsConfig(AWSProperty):
    props = ...

class ProjectSourceVersion(AWSProperty):
    props = ...

class ProjectFileSystemLocation(AWSProperty):
    props = ...

class Project(AWSObject):
    resource_type = ...
    props = ...

class S3ReportExportConfig(AWSProperty):
    props = ...

class ReportExportConfig(AWSProperty):
    props = ...

class ReportGroup(AWSObject):
    resource_type = ...
    props = ...

class SourceCredential(AWSObject):
    resource_type = ...
    props = ...
