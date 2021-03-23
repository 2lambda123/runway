"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Elemental MediaTailor"
prefix = "mediatailor"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

DeletePlaybackConfiguration = Action("DeletePlaybackConfiguration")
GetPlaybackConfiguration = Action("GetPlaybackConfiguration")
ListPlaybackConfigurations = Action("ListPlaybackConfigurations")
ListTagsForResource = Action("ListTagsForResource")
PutPlaybackConfiguration = Action("PutPlaybackConfiguration")
TagResource = Action("TagResource")
UntagResource = Action("UntagResource")