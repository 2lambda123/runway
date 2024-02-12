"""
This type stub file was generated by pyright.
"""

import logging

from botocore.retries.base import BaseRetryableChecker, BaseRetryBackoff

"""Standard retry behavior.

This contains the default standard retry behavior.
It provides consistent behavior with other AWS SDKs.

The key base classes uses for retries:

    * ``BaseRetryableChecker`` - Use to check a specific condition that
    indicates a retry should happen.  This can include things like
    max attempts, HTTP status code checks, error code checks etc.
    * ``RetryBackoff`` - Use to determine how long we should backoff until
    we retry a request.  This is the class that will implement delay such
    as exponential backoff.
    * ``RetryPolicy`` - Main class that determines if a retry should
    happen.  It can combine data from a various BaseRetryableCheckers
    to make a final call as to whether or not a retry should happen.
    It then uses a ``BaseRetryBackoff`` to determine how long to delay.
    * ``RetryHandler`` - The bridge between botocore's event system
    used by endpoint.py to manage retries and the interfaces defined
    in this module.

This allows us to define an API that has minimal coupling to the event
based API used by botocore.

"""
DEFAULT_MAX_ATTEMPTS = 3
logger = logging.getLogger(__name__)

def register_retry_handler(client, max_attempts=...): ...

class RetryHandler(object):
    """Bridge between botocore's event system and this module.

    This class is intended to be hooked to botocore's event system
    as an event handler.
    """

    def __init__(self, retry_policy, retry_event_adapter, retry_quota) -> None: ...
    def needs_retry(self, **kwargs):
        """Connect as a handler to the needs-retry event."""
        ...

class RetryEventAdapter(object):
    """Adapter to existing retry interface used in the endpoints layer.

    This existing interface for determining if a retry needs to happen
    is event based and used in ``botocore.endpoint``.  The interface has
    grown organically over the years and could use some cleanup.  This
    adapter converts that interface into the interface used by the
    new retry strategies.

    """

    def create_retry_context(self, **kwargs):
        """Create context based on needs-retry kwargs."""
        ...

    def adapt_retry_response_from_context(self, context):
        """Modify response back to user back from context."""
        ...

class RetryContext(object):
    """Normalize a response that we use to check if a retry should occur.

    This class smoothes over the different types of responses we may get
    from a service including:

        * A modeled error response from the service that contains a service
          code and error message.
        * A raw HTTP response that doesn't contain service protocol specific
          error keys.
        * An exception received while attempting to retrieve a response.
          This could be a ConnectionError we receive from our HTTP layer which
          could represent that we weren't able to receive a response from
          the service.

    This class guarantees that at least one of the above attributes will be
    non None.

    This class is meant to provide a read-only view into the properties
    associated with a possible retryable response.  None of the properties
    are meant to be modified directly.

    """

    def __init__(
        self,
        attempt_number,
        operation_model=...,
        parsed_response=...,
        http_response=...,
        caught_exception=...,
        request_context=...,
    ) -> None: ...
    def get_error_code(self):
        """Check if there was a parsed response with an error code.

        If we could not find any error codes, ``None`` is returned.

        """
        ...

    def add_retry_metadata(self, **kwargs):
        """Add key/value pairs to the retry metadata.

        This allows any objects during the retry process to add
        metadata about any checks/validations that happened.

        This gets added to the response metadata in the retry handler.

        """
        ...

    def get_retry_metadata(self): ...

class RetryPolicy(object):
    def __init__(self, retry_checker, retry_backoff) -> None: ...
    def should_retry(self, context): ...
    def compute_retry_delay(self, context): ...

class ExponentialBackoff(BaseRetryBackoff):
    _BASE = ...
    _MAX_BACKOFF = ...
    def __init__(self, max_backoff=..., random=...) -> None: ...
    def delay_amount(self, context):
        """Calculates delay based on exponential backoff.

        This class implements truncated binary exponential backoff
        with jitter::

            t_i = min(rand(0, 1) * 2 ** attempt, MAX_BACKOFF)

        where ``i`` is the request attempt (0 based).

        """
        ...

class MaxAttemptsChecker(BaseRetryableChecker):
    def __init__(self, max_attempts) -> None: ...
    def is_retryable(self, context): ...

class TransientRetryableChecker(BaseRetryableChecker):
    _TRANSIENT_ERROR_CODES = ...
    _TRANSIENT_STATUS_CODES = ...
    _TRANSIENT_EXCEPTION_CLS = ...
    def __init__(
        self,
        transient_error_codes=...,
        transient_status_codes=...,
        transient_exception_cls=...,
    ) -> None: ...
    def is_retryable(self, context): ...

class ThrottledRetryableChecker(BaseRetryableChecker):
    _THROTTLED_ERROR_CODES = ...
    def __init__(self, throttled_error_codes=...) -> None: ...
    def is_retryable(self, context): ...

class ModeledRetryableChecker(BaseRetryableChecker):
    """Check if an error has been modeled as retryable."""

    def __init__(self) -> None: ...
    def is_retryable(self, context): ...

class ModeledRetryErrorDetector(object):
    """Checks whether or not an error is a modeled retryable error."""

    TRANSIENT_ERROR = ...
    THROTTLING_ERROR = ...
    def detect_error_type(self, context):
        """Detect the error type associated with an error code and model.

        This will either return:

            * ``self.TRANSIENT_ERROR`` - If the error is a transient error
            * ``self.THROTTLING_ERROR`` - If the error is a throttling error
            * ``None`` - If the error is neither type of error.

        """
        ...

class ThrottlingErrorDetector(object):
    def __init__(self, retry_event_adapter) -> None: ...
    def is_throttling_error(self, **kwargs): ...

class StandardRetryConditions(BaseRetryableChecker):
    """Concrete class that implements the standard retry policy checks.

    Specifically:

        not max_attempts and (transient or throttled or modeled_retry)

    """

    def __init__(self, max_attempts=...) -> None: ...
    def is_retryable(self, context): ...

class OrRetryChecker(BaseRetryableChecker):
    def __init__(self, checkers) -> None: ...
    def is_retryable(self, context): ...

class RetryQuotaChecker(object):
    _RETRY_COST = ...
    _NO_RETRY_INCREMENT = ...
    _TIMEOUT_RETRY_REQUEST = ...
    _TIMEOUT_EXCEPTIONS = ...
    def __init__(self, quota) -> None: ...
    def acquire_retry_quota(self, context): ...
    def release_retry_quota(self, context, http_response, **kwargs): ...
