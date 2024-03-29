"""
This type stub file was generated by pyright.
"""

import logging

logger = logging.getLogger(__name__)
EMPTY_SHA256_HASH = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
PAYLOAD_BUFFER = 1024 * 1024
ISO8601 = "%Y-%m-%dT%H:%M:%SZ"
SIGV4_TIMESTAMP = "%Y%m%dT%H%M%SZ"
SIGNED_HEADERS_BLACKLIST = ["expect", "user-agent", "x-amzn-trace-id"]
UNSIGNED_PAYLOAD = "UNSIGNED-PAYLOAD"

class BaseSigner(object):
    REQUIRES_REGION = ...
    def add_auth(self, request): ...

class SigV2Auth(BaseSigner):
    """
    Sign a request with Signature V2.
    """

    def __init__(self, credentials) -> None: ...
    def calc_signature(self, request, params): ...
    def add_auth(self, request): ...

class SigV3Auth(BaseSigner):
    def __init__(self, credentials) -> None: ...
    def add_auth(self, request): ...

class SigV4Auth(BaseSigner):
    """
    Sign a request with Signature V4.
    """

    REQUIRES_REGION = ...
    def __init__(self, credentials, service_name, region_name) -> None: ...
    def headers_to_sign(self, request):
        """
        Select the headers from the request that need to be included
        in the StringToSign.
        """
        ...

    def canonical_query_string(self, request): ...
    def canonical_headers(self, headers_to_sign):
        """
        Return the headers that need to be included in the StringToSign
        in their canonical form by converting all header keys to lower
        case, sorting them in alphabetical order and then joining
        them into a string, separated by newlines.
        """
        ...

    def signed_headers(self, headers_to_sign): ...
    def payload(self, request): ...
    def canonical_request(self, request): ...
    def scope(self, request): ...
    def credential_scope(self, request): ...
    def string_to_sign(self, request, canonical_request):
        """
        Return the canonical StringToSign as well as a dict
        containing the original version of all headers that
        were included in the StringToSign.
        """
        ...

    def signature(self, string_to_sign, request): ...
    def add_auth(self, request): ...

class S3SigV4Auth(SigV4Auth): ...

class SigV4QueryAuth(SigV4Auth):
    DEFAULT_EXPIRES = ...
    def __init__(self, credentials, service_name, region_name, expires=...) -> None: ...

class S3SigV4QueryAuth(SigV4QueryAuth):
    """S3 SigV4 auth using query parameters.

    This signer will sign a request using query parameters and signature
    version 4, i.e a "presigned url" signer.

    Based off of:

    http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html

    """

    def payload(self, request): ...

class S3SigV4PostAuth(SigV4Auth):
    """
    Presigns a s3 post

    Implementation doc here:
    http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-UsingHTTPPOST.html
    """

    def add_auth(self, request): ...

class HmacV1Auth(BaseSigner):
    QSAOfInterest = ...
    def __init__(self, credentials, service_name=..., region_name=...) -> None: ...
    def sign_string(self, string_to_sign): ...
    def canonical_standard_headers(self, headers): ...
    def canonical_custom_headers(self, headers): ...
    def unquote_v(self, nv):
        """
        TODO: Do we need this?
        """
        ...

    def canonical_resource(self, split, auth_path=...): ...
    def canonical_string(self, method, split, headers, expires=..., auth_path=...): ...
    def get_signature(self, method, split, headers, expires=..., auth_path=...): ...
    def add_auth(self, request): ...

class HmacV1QueryAuth(HmacV1Auth):
    """
    Generates a presigned request for s3.

    Spec from this document:

    http://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html
    #RESTAuthenticationQueryStringAuth

    """

    DEFAULT_EXPIRES = ...
    def __init__(self, credentials, expires=...) -> None: ...

class HmacV1PostAuth(HmacV1Auth):
    """
    Generates a presigned post for s3.

    Spec from this document:

    http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingHTTPPOST.html
    """

    def add_auth(self, request): ...

AUTH_TYPE_MAPS = {
    "v2": SigV2Auth,
    "v4": SigV4Auth,
    "v4-query": SigV4QueryAuth,
    "v3": SigV3Auth,
    "v3https": SigV3Auth,
    "s3": HmacV1Auth,
    "s3-query": HmacV1QueryAuth,
    "s3-presign-post": HmacV1PostAuth,
    "s3v4": S3SigV4Auth,
    "s3v4-query": S3SigV4QueryAuth,
    "s3v4-presign-post": S3SigV4PostAuth,
}
