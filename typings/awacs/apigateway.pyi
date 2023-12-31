"""
This type stub file was generated by pyright.
"""

from .aws import Action as BaseAction
from .aws import BaseARN

service_name = "Manage Amazon API Gateway"
prefix = "apigateway"

class Action(BaseAction):
    def __init__(self, action=...) -> None: ...

class ARN(BaseARN):
    def __init__(self, resource=..., region=..., account=...) -> None: ...

DELETE = Action("DELETE")
GET = Action("GET")
HEAD = Action("HEAD")
OPTIONS = Action("OPTIONS")
PATCH = Action("PATCH")
POST = Action("POST")
PUT = Action("PUT")
SetWebACL = Action("SetWebACL")
UpdateRestApiPolicy = Action("UpdateRestApiPolicy")
