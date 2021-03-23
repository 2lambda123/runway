"""
This type stub file was generated by pyright.
"""

import logging
import os
import re

__version__ = "1.19.56"

class NullHandler(logging.Handler):
    def emit(self, record): ...

log = logging.getLogger("botocore")
_first_cap_regex = re.compile("(.)([A-Z][a-z]+)")
_end_cap_regex = re.compile("([a-z0-9])([A-Z])")
_special_case_transform = re.compile("[A-Z]{3,}s$")
_xform_cache = {
    ("CreateCachediSCSIVolume", "_"): "create_cached_iscsi_volume",
    ("CreateCachediSCSIVolume", "-"): "create-cached-iscsi-volume",
    ("DescribeCachediSCSIVolumes", "_"): "describe_cached_iscsi_volumes",
    ("DescribeCachediSCSIVolumes", "-"): "describe-cached-iscsi-volumes",
    ("DescribeStorediSCSIVolumes", "_"): "describe_stored_iscsi_volumes",
    ("DescribeStorediSCSIVolumes", "-"): "describe-stored-iscsi-volumes",
    ("CreateStorediSCSIVolume", "_"): "create_stored_iscsi_volume",
    ("CreateStorediSCSIVolume", "-"): "create-stored-iscsi-volume",
    ("ListHITsForQualificationType", "_"): "list_hits_for_qualification_type",
    ("ListHITsForQualificationType", "-"): "list-hits-for-qualification-type",
    ("ExecutePartiQLStatement", "_"): "execute_partiql_statement",
    ("ExecutePartiQLStatement", "-"): "execute-partiql-statement",
    ("ExecutePartiQLTransaction", "_"): "execute_partiql_transaction",
    ("ExecutePartiQLTransaction", "-"): "execute-partiql-transaction",
    ("ExecutePartiQLBatch", "_"): "execute_partiql_batch",
    ("ExecutePartiQLBatch", "-"): "execute-partiql-batch",
}
ScalarTypes = ("string", "integer", "boolean", "timestamp", "float", "double")
BOTOCORE_ROOT = os.path.dirname(os.path.abspath(__file__))

class UNSIGNED(object):
    def __copy__(self): ...
    def __deepcopy__(self, memodict): ...

UNSIGNED = UNSIGNED()

def xform_name(name, sep=..., _xform_cache=...):
    """Convert camel case to a "pythonic" name.

    If the name contains the ``sep`` character, then it is
    returned unchanged.

    """
    ...