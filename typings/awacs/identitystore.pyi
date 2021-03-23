"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "AWS Identity Store"
prefix = "identitystore"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

DescribeGroup = Action("DescribeGroup")
DescribeUser = Action("DescribeUser")
ListGroups = Action("ListGroups")
ListUsers = Action("ListUsers")