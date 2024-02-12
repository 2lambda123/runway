"""
This type stub file was generated by pyright.
"""

import logging
import re

from botocore.exceptions import (
    ConnectionClosedError,
    ConnectTimeoutError,
    EndpointConnectionError,
    ReadTimeoutError,
)

logger = logging.getLogger(__name__)
DEFAULT_METADATA_SERVICE_TIMEOUT = 1
METADATA_BASE_URL = "http://169.254.169.254/"
METADATA_BASE_URL_IPv6 = "http://[fe80:ec2::254%eth0]/"
SAFE_CHARS = "-._~"
LABEL_RE = re.compile(r"[a-z0-9][a-z0-9\-]*[a-z0-9]")
RETRYABLE_HTTP_ERRORS = (
    ReadTimeoutError,
    EndpointConnectionError,
    ConnectionClosedError,
    ConnectTimeoutError,
)
S3_ACCELERATE_WHITELIST = ["dualstack"]
EVENT_ALIASES = {
    "a4b": "alexa-for-business",
    "alexaforbusiness": "alexa-for-business",
    "api.mediatailor": "mediatailor",
    "api.pricing": "pricing",
    "api.sagemaker": "sagemaker",
    "apigateway": "api-gateway",
    "application-autoscaling": "application-auto-scaling",
    "appstream2": "appstream",
    "autoscaling": "auto-scaling",
    "autoscaling-plans": "auto-scaling-plans",
    "ce": "cost-explorer",
    "cloudhsmv2": "cloudhsm-v2",
    "cloudsearchdomain": "cloudsearch-domain",
    "cognito-idp": "cognito-identity-provider",
    "config": "config-service",
    "cur": "cost-and-usage-report-service",
    "data.iot": "iot-data-plane",
    "data.jobs.iot": "iot-jobs-data-plane",
    "data.mediastore": "mediastore-data",
    "datapipeline": "data-pipeline",
    "devicefarm": "device-farm",
    "devices.iot1click": "iot-1click-devices-service",
    "directconnect": "direct-connect",
    "discovery": "application-discovery-service",
    "dms": "database-migration-service",
    "ds": "directory-service",
    "dynamodbstreams": "dynamodb-streams",
    "elasticbeanstalk": "elastic-beanstalk",
    "elasticfilesystem": "efs",
    "elasticloadbalancing": "elastic-load-balancing",
    "elasticmapreduce": "emr",
    "elastictranscoder": "elastic-transcoder",
    "elb": "elastic-load-balancing",
    "elbv2": "elastic-load-balancing-v2",
    "email": "ses",
    "entitlement.marketplace": "marketplace-entitlement-service",
    "es": "elasticsearch-service",
    "events": "eventbridge",
    "cloudwatch-events": "eventbridge",
    "iot-data": "iot-data-plane",
    "iot-jobs-data": "iot-jobs-data-plane",
    "iot1click-devices": "iot-1click-devices-service",
    "iot1click-projects": "iot-1click-projects",
    "kinesisanalytics": "kinesis-analytics",
    "kinesisvideo": "kinesis-video",
    "lex-models": "lex-model-building-service",
    "lex-runtime": "lex-runtime-service",
    "logs": "cloudwatch-logs",
    "machinelearning": "machine-learning",
    "marketplace-entitlement": "marketplace-entitlement-service",
    "marketplacecommerceanalytics": "marketplace-commerce-analytics",
    "metering.marketplace": "marketplace-metering",
    "meteringmarketplace": "marketplace-metering",
    "mgh": "migration-hub",
    "models.lex": "lex-model-building-service",
    "monitoring": "cloudwatch",
    "mturk-requester": "mturk",
    "opsworks-cm": "opsworkscm",
    "projects.iot1click": "iot-1click-projects",
    "resourcegroupstaggingapi": "resource-groups-tagging-api",
    "route53": "route-53",
    "route53domains": "route-53-domains",
    "runtime.lex": "lex-runtime-service",
    "runtime.sagemaker": "sagemaker-runtime",
    "sdb": "simpledb",
    "secretsmanager": "secrets-manager",
    "serverlessrepo": "serverlessapplicationrepository",
    "servicecatalog": "service-catalog",
    "states": "sfn",
    "stepfunctions": "sfn",
    "storagegateway": "storage-gateway",
    "streams.dynamodb": "dynamodb-streams",
    "tagging": "resource-groups-tagging-api",
}
IPV4_PAT = r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}"
HEX_PAT = "[0-9A-Fa-f]{1,4}"
LS32_PAT = "(?:{hex}:{hex}|{ipv4})".format(hex=HEX_PAT, ipv4=IPV4_PAT)
_subs = {"hex": HEX_PAT, "ls32": LS32_PAT}
_variations = [
    "(?:%(hex)s:){6}%(ls32)s",
    "::(?:%(hex)s:){5}%(ls32)s",
    "(?:%(hex)s)?::(?:%(hex)s:){4}%(ls32)s",
    "(?:(?:%(hex)s:)?%(hex)s)?::(?:%(hex)s:){3}%(ls32)s",
    "(?:(?:%(hex)s:){0,2}%(hex)s)?::(?:%(hex)s:){2}%(ls32)s",
    "(?:(?:%(hex)s:){0,3}%(hex)s)?::%(hex)s:%(ls32)s",
    "(?:(?:%(hex)s:){0,4}%(hex)s)?::%(ls32)s",
    "(?:(?:%(hex)s:){0,5}%(hex)s)?::%(hex)s",
    "(?:(?:%(hex)s:){0,6}%(hex)s)?::",
]
UNRESERVED_PAT = r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._!\-~"
IPV6_PAT = "(?:" + "|".join([x % _subs for x in _variations]) + ")"
ZONE_ID_PAT = "(?:%25|%)(?:[" + UNRESERVED_PAT + "]|%[a-fA-F0-9]{2})+"
IPV6_ADDRZ_PAT = r"\[" + IPV6_PAT + r"(?:" + ZONE_ID_PAT + r")?\]"
IPV6_ADDRZ_RE = re.compile("^" + IPV6_ADDRZ_PAT + "$")

def ensure_boolean(val):
    """Ensures a boolean value if a string or boolean is provided

    For strings, the value for True/False is case insensitive
    """
    ...

def is_json_value_header(shape):
    """Determines if the provided shape is the special header type jsonvalue.

    :type shape: botocore.shape
    :param shape: Shape to be inspected for the jsonvalue trait.

    :return: True if this type is a jsonvalue, False otherwise
    :rtype: Bool
    """
    ...

def get_service_module_name(service_model):
    """Returns the module name for a service

    This is the value used in both the documentation and client class name
    """
    ...

def normalize_url_path(path): ...
def normalize_boolean(val):
    """Returns None if val is None, otherwise ensure value
    converted to boolean"""
    ...

def remove_dot_segments(url): ...
def validate_jmespath_for_set(expression): ...
def set_value_from_jmespath(source, expression, value, is_first=...): ...

class _RetriesExceededError(Exception):
    """Internal exception used when the number of retries are exceeded."""

    ...

class BadIMDSRequestError(Exception):
    def __init__(self, request) -> None: ...

class IMDSFetcher(object):
    _RETRIES_EXCEEDED_ERROR_CLS = ...
    _TOKEN_PATH = ...
    _TOKEN_TTL = ...
    def __init__(
        self,
        timeout=...,
        num_attempts=...,
        base_url=...,
        env=...,
        user_agent=...,
        config=...,
    ) -> None: ...
    def get_base_url(self): ...

class InstanceMetadataFetcher(IMDSFetcher):
    _URL_PATH = ...
    _REQUIRED_CREDENTIAL_FIELDS = ...
    def retrieve_iam_role_credentials(self): ...

def merge_dicts(dict1, dict2, append_lists=...):
    """Given two dict, merge the second dict into the first.

    The dicts can have arbitrary nesting.

    :param append_lists: If true, instead of clobbering a list with the new
        value, append all of the new values onto the original list.
    """
    ...

def lowercase_dict(original):
    """Copies the given dictionary ensuring all keys are lowercase strings."""
    ...

def parse_key_val_file(filename, _open=...): ...
def parse_key_val_file_contents(contents): ...
def percent_encode_sequence(mapping, safe=...):
    """Urlencode a dict or list into a string.

    This is similar to urllib.urlencode except that:

    * It uses quote, and not quote_plus
    * It has a default list of safe chars that don't need
      to be encoded, which matches what AWS services expect.

    If any value in the input ``mapping`` is a list type,
    then each list element wil be serialized.  This is the equivalent
    to ``urlencode``'s ``doseq=True`` argument.

    This function should be preferred over the stdlib
    ``urlencode()`` function.

    :param mapping: Either a dict to urlencode or a list of
        ``(key, value)`` pairs.

    """
    ...

def percent_encode(input_str, safe=...):
    """Urlencodes a string.

    Whereas percent_encode_sequence handles taking a dict/sequence and
    producing a percent encoded string, this function deals only with
    taking a string (not a dict/sequence) and percent encoding it.

    If given the binary type, will simply URL encode it. If given the
    text type, will produce the binary type by UTF-8 encoding the
    text. If given something else, will convert it to the text type
    first.
    """
    ...

def parse_timestamp(value):
    """Parse a timestamp into a datetime object.

    Supported formats:

        * iso8601
        * rfc822
        * epoch (value is an integer)

    This will return a ``datetime.datetime`` object.

    """
    ...

def parse_to_aware_datetime(value):
    """Converted the passed in value to a datetime object with tzinfo.

    This function can be used to normalize all timestamp inputs.  This
    function accepts a number of different types of inputs, but
    will always return a datetime.datetime object with time zone
    information.

    The input param ``value`` can be one of several types:

        * A datetime object (both naive and aware)
        * An integer representing the epoch time (can also be a string
          of the integer, i.e '0', instead of 0).  The epoch time is
          considered to be UTC.
        * An iso8601 formatted timestamp.  This does not need to be
          a complete timestamp, it can contain just the date portion
          without the time component.

    The returned value will be a datetime object that will have tzinfo.
    If no timezone info was provided in the input value, then UTC is
    assumed, not local time.

    """
    ...

def datetime2timestamp(dt, default_timezone=...):
    """Calculate the timestamp based on the given datetime instance.

    :type dt: datetime
    :param dt: A datetime object to be converted into timestamp
    :type default_timezone: tzinfo
    :param default_timezone: If it is provided as None, we treat it as tzutc().
                             But it is only used when dt is a naive datetime.
    :returns: The timestamp
    """
    ...

def calculate_sha256(body, as_hex=...):
    """Calculate a sha256 checksum.

    This method will calculate the sha256 checksum of a file like
    object.  Note that this method will iterate through the entire
    file contents.  The caller is responsible for ensuring the proper
    starting position of the file and ``seek()``'ing the file back
    to its starting location if other consumers need to read from
    the file like object.

    :param body: Any file like object.  The file must be opened
        in binary mode such that a ``.read()`` call returns bytes.
    :param as_hex: If True, then the hex digest is returned.
        If False, then the digest (as binary bytes) is returned.

    :returns: The sha256 checksum

    """
    ...

def calculate_tree_hash(body):
    """Calculate a tree hash checksum.

    For more information see:

    http://docs.aws.amazon.com/amazonglacier/latest/dev/checksum-calculations.html

    :param body: Any file like object.  This has the same constraints as
        the ``body`` param in calculate_sha256

    :rtype: str
    :returns: The hex version of the calculated tree hash

    """
    ...

class CachedProperty(object):
    """A read only property that caches the initially computed value.

    This descriptor will only call the provided ``fget`` function once.
    Subsequent access to this property will return the cached value.

    """

    def __init__(self, fget) -> None: ...
    def __get__(self, obj, cls): ...

class ArgumentGenerator(object):
    """Generate sample input based on a shape model.

    This class contains a ``generate_skeleton`` method that will take
    an input/output shape (created from ``botocore.model``) and generate
    a sample dictionary corresponding to the input/output shape.

    The specific values used are place holder values. For strings either an
    empty string or the member name can be used, for numbers 0 or 0.0 is used.
    The intended usage of this class is to generate the *shape* of the input
    structure.

    This can be useful for operations that have complex input shapes.
    This allows a user to just fill in the necessary data instead of
    worrying about the specific structure of the input arguments.

    Example usage::

        s = botocore.session.get_session()
        ddb = s.get_service_model('dynamodb')
        arg_gen = ArgumentGenerator()
        sample_input = arg_gen.generate_skeleton(
            ddb.operation_model('CreateTable').input_shape)
        print("Sample input for dynamodb.CreateTable: %s" % sample_input)

    """

    def __init__(self, use_member_names=...) -> None: ...
    def generate_skeleton(self, shape):
        """Generate a sample input.

        :type shape: ``botocore.model.Shape``
        :param shape: The input shape.

        :return: The generated skeleton input corresponding to the
            provided input shape.

        """
        ...

def is_valid_ipv6_endpoint_url(endpoint_url): ...
def is_valid_endpoint_url(endpoint_url):
    """Verify the endpoint_url is valid.

    :type endpoint_url: string
    :param endpoint_url: An endpoint_url.  Must have at least a scheme
        and a hostname.

    :return: True if the endpoint url is valid. False otherwise.

    """
    ...

def is_valid_uri(endpoint_url): ...
def validate_region_name(region_name):
    """Provided region_name must be a valid host label."""
    ...

def check_dns_name(bucket_name):
    """
    Check to see if the ``bucket_name`` complies with the
    restricted DNS naming conventions necessary to allow
    access via virtual-hosting style.

    Even though "." characters are perfectly valid in this DNS
    naming scheme, we are going to punt on any name containing a
    "." character because these will cause SSL cert validation
    problems if we try to use virtual-hosting style addressing.
    """
    ...

def fix_s3_host(
    request, signature_version, region_name, default_endpoint_url=..., **kwargs
):
    """
    This handler looks at S3 requests just before they are signed.
    If there is a bucket name on the path (true for everything except
    ListAllBuckets) it checks to see if that bucket name conforms to
    the DNS naming conventions.  If it does, it alters the request to
    use ``virtual hosting`` style addressing rather than ``path-style``
    addressing.

    """
    ...

def switch_to_virtual_host_style(
    request, signature_version, default_endpoint_url=..., **kwargs
):
    """
    This is a handler to force virtual host style s3 addressing no matter
    the signature version (which is taken in consideration for the default
    case). If the bucket is not DNS compatible an InvalidDNSName is thrown.

    :param request: A AWSRequest object that is about to be sent.
    :param signature_version: The signature version to sign with
    :param default_endpoint_url: The endpoint to use when switching to a
        virtual style. If None is supplied, the virtual host will be
        constructed from the url of the request.
    """
    ...

def instance_cache(func):
    """Method decorator for caching method calls to a single instance.

    **This is not a general purpose caching decorator.**

    In order to use this, you *must* provide an ``_instance_cache``
    attribute on the instance.

    This decorator is used to cache method calls.  The cache is only
    scoped to a single instance though such that multiple instances
    will maintain their own cache.  In order to keep things simple,
    this decorator requires that you provide an ``_instance_cache``
    attribute on your instance.

    """
    ...

def switch_host_s3_accelerate(request, operation_name, **kwargs):
    """Switches the current s3 endpoint with an S3 Accelerate endpoint"""
    ...

def switch_host_with_param(request, param_name):
    """Switches the host using a parameter value from a JSON request body"""
    ...

def deep_merge(base, extra):
    """Deeply two dictionaries, overriding existing keys in the base.

    :param base: The base dictionary which will be merged into.
    :param extra: The dictionary to merge into the base. Keys from this
        dictionary will take precedence.
    """
    ...

def hyphenize_service_id(service_id):
    """Translate the form used for event emitters.

    :param service_id: The service_id to convert.
    """
    ...

class S3RegionRedirector(object):
    def __init__(self, endpoint_bridge, client, cache=...) -> None: ...
    def register(self, event_emitter=...): ...
    def redirect_from_error(self, request_dict, response, operation, **kwargs):
        """
        An S3 request sent to the wrong region will return an error that
        contains the endpoint the request should be sent to. This handler
        will add the redirect information to the signing context and then
        redirect the request.
        """
        ...

    def get_bucket_region(self, bucket, response):
        """
        There are multiple potential sources for the new region to redirect to,
        but they aren't all universally available for use. This will try to
        find region from response elements, but will fall back to calling
        HEAD on the bucket if all else fails.

        :param bucket: The bucket to find the region for. This is necessary if
            the region is not available in the error response.
        :param response: A response representing a service request that failed
            due to incorrect region configuration.
        """
        ...

    def set_request_url(self, params, context, **kwargs): ...
    def redirect_from_cache(self, params, context, **kwargs):
        """
        This handler retrieves a given bucket's signing context from the cache
        and adds it into the request context.
        """
        ...

class InvalidArnException(ValueError): ...

class ArnParser(object):
    def parse_arn(self, arn): ...

class S3ArnParamHandler(object):
    _RESOURCE_REGEX = ...
    _OUTPOST_RESOURCE_REGEX = ...
    _BLACKLISTED_OPERATIONS = ...
    def __init__(self, arn_parser=...) -> None: ...
    def register(self, event_emitter): ...
    def handle_arn(self, params, model, context, **kwargs): ...

class S3EndpointSetter(object):
    _DEFAULT_PARTITION = ...
    _DEFAULT_DNS_SUFFIX = ...
    def __init__(
        self,
        endpoint_resolver,
        region=...,
        s3_config=...,
        endpoint_url=...,
        partition=...,
    ) -> None: ...
    def register(self, event_emitter): ...
    def set_endpoint(self, request, **kwargs): ...

class S3ControlEndpointSetter(object):
    _DEFAULT_PARTITION = ...
    _DEFAULT_DNS_SUFFIX = ...
    _HOST_LABEL_REGEX = ...
    def __init__(
        self,
        endpoint_resolver,
        region=...,
        s3_config=...,
        endpoint_url=...,
        partition=...,
    ) -> None: ...
    def register(self, event_emitter): ...
    def set_endpoint(self, request, **kwargs): ...

class S3ControlArnParamHandler(object):
    _RESOURCE_SPLIT_REGEX = ...
    def __init__(self, arn_parser=...) -> None: ...
    def register(self, event_emitter): ...
    def handle_arn(self, params, model, context, **kwargs): ...

class ContainerMetadataFetcher(object):
    TIMEOUT_SECONDS = ...
    RETRY_ATTEMPTS = ...
    SLEEP_TIME = ...
    IP_ADDRESS = ...
    _ALLOWED_HOSTS = ...
    def __init__(self, session=..., sleep=...) -> None: ...
    def retrieve_full_uri(self, full_url, headers=...):
        """Retrieve JSON metadata from container metadata.

        :type full_url: str
        :param full_url: The full URL of the metadata service.
            This should include the scheme as well, e.g
            "http://localhost:123/foo"

        """
        ...

    def retrieve_uri(self, relative_uri):
        """Retrieve JSON metadata from ECS metadata.

        :type relative_uri: str
        :param relative_uri: A relative URI, e.g "/foo/bar?id=123"

        :return: The parsed JSON response.

        """
        ...

    def full_url(self, relative_uri): ...

def get_environ_proxies(url): ...
def should_bypass_proxies(url):
    """
    Returns whether we should bypass proxies or not.
    """
    ...

def get_encoding_from_headers(headers, default=...):
    """Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :param default: default encoding if the content-type is text
    """
    ...

def calculate_md5(body, **kwargs): ...
def conditionally_calculate_md5(params, **kwargs):
    """Only add a Content-MD5 if the system supports it."""
    ...

class FileWebIdentityTokenLoader(object):
    def __init__(self, web_identity_token_path, _open=...) -> None: ...
    def __call__(self): ...

class SSOTokenLoader(object):
    def __init__(self, cache=...) -> None: ...
    def __call__(self, start_url): ...
