import enum

BASE_URL: str = ...

class InvalidDog(ValueError): ...

class StatusCode(enum.Enum):
    CONTINUE: int = ...
    SWITCHING_PROTOCOLS: int = ...
    PROCESSING: int = ...
    OK: int = ...
    SUCCESS: int = ...
    CREATED: int = ...
    ACCEPTED: int = ...
    NO_CONTENT: int = ...
    PARTIAL_CONTENT: int = ...
    MULTI_STATUS: int = ...
    MULTIPLE_CHOICES: int = ...
    MOVED_PERMANENTLY: int = ...
    FOUND: int = ...
    SEE_OTHER: int = ...
    NOT_MODIFIED: int = ...
    USE_PROXY: int = ...
    TEMPORARY_REDIRECT: int = ...
    BAD_REQUEST: int = ...
    UNAUTHORIZED: int = ...
    PAYMENT_REQUIRED: int = ...
    FORBIDDEN: int = ...
    NOT_FOUND: int = ...
    METHOD_NOT_ALLOWED: int = ...
    NOT_ACCEPTABLE: int = ...
    REQUEST_TIMEOUT: int = ...
    CONFLICT: int = ...
    GONE: int = ...
    LENGTH_REQUIRED: int = ...
    PRECONDITION_FAILED: int = ...
    PAYLOAD_TOO_LARGE: int = ...
    REQUEST_URI_TOO_LONG: int = ...
    UNSUPPORTED_MEDIA_TYPE: int = ...
    REQUEST_RANGE_NOT_SATISFIABLE: int = ...
    EXPECTATION_FAILED: int = ...
    IM_A_TEAPOT: int = ...
    ENHANCE_YOUR_CALM: int = ...
    MISDIRECTED_REQUEST: int = ...
    UNPROCESSABLE_ENTITY: int = ...
    LOCKED: int = ...
    FAILED_DEPENDENCY: int = ...
    UNORDERED_COLLECTION: int = ...
    UPGRADE_REQUIRED: int = ...
    TOO_MANY_REQUESTS: int = ...
    REQUEST_HEADER_FIELDS_TOO_LARGE: int = ...
    NO_RESPONSE: int = ...
    BLOCKED_BY_WINDOWS_PARENTAL_CONTROLS: int = ...
    UNAVAILABLE_FOR_LEGAL_REASONS: int = ...
    CLIENT_CLOSED_REQUEST: int = ...
    INTERNAL_SERVER_ERROR: int = ...
    NOT_IMPLEMENTED: int = ...
    BAD_GATEWAY: int = ...
    SERVICE_UNAVAILABLE: int = ...
    GATEWAY_TIMEOUT: int = ...
    VARIANT_ALSO_NEGOTIATES: int = ...
    INSUFFICIENT_STORAGE: int = ...
    LOOP_DETECTED: int = ...
    BANDWIDTH_LIMIT_EXCEEDED: int = ...
    NOT_EXTENDED: int = ...
    NETWORK_AUTHENTICATION_REQUIRED: int = ...
    NETWORK_CONNECT_TIMEOUT_ERROR: int = ...

class HTTPDog:
    code: int = ...
    name: str = ...
    url: str = ...
    description: str = ...
    image: bytes = ...
    image_url: str = ...
    def __init__(self, code: int, name: str, url: str, description: str, image: bytes, image_url: str) -> None: ...
    def __int__(self) -> int: ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...

def dog_by_code(code: int) -> HTTPDog: ...
def dog_by_name(name: str) -> HTTPDog: ...