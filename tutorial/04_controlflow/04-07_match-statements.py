# Chapter 4.7: match Statements (Structural Pattern Matching)
# Ref: https://docs.python.org/3/tutorial/controlflow.html#match-statements
# Requires Python 3.10+


# ============================================================
# [block-1] Basic match syntax
# Unlike switch in C/Java, Python match does NOT fall through.
# If no case matches, nothing happens (no error, no default needed).
# ============================================================
def describe_status(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"


print(describe_status(200))  # OK
print(describe_status(404))  # Not Found
print(describe_status(500))  # Internal Server Error
print(describe_status(999))  # Unknown status


# ============================================================
# [block-2] Literal pattern + wildcard pattern (case _:)
# case _: acts as the "catch-all" / default branch.
# It always matches and must come last.
# ============================================================
def http_method_level(method: str) -> str:
    match method.upper():
        case "GET":
            return "Read Resource"
        case "POST":
            return "Create resource"
        case "PUT" | "PATCH":
            # OR pattern: matched either value
            return "Update resource"
        case "DELETE":
            return "Delete resource"
        case _:
            # Wildcard: matches anything not caught above
            return f"Unsupported method: {method}"


print(http_method_level("GET"))  # Read Resource
print(http_method_level("POST"))  # Create resource
print(http_method_level("PUT"))  # Update resource
print(http_method_level("PATCH"))  # Update resource
print(http_method_level("DELETE"))  # Delete resource
print(http_method_level("HEAD"))  # Unsupported method: HEAD


# ============================================================
# [block-3] OR pattern  (case A | B | C:)
# Groups multiple values into a single branch.
# Common use: grouping HTTP error codes by category.
# ============================================================
def classify_http_error(code: int) -> str:
    match code:
        case 400:
            return "Bad request"
        case 401 | 403:
            # OR pattern: authentication / authorization errors
            return "Auth error (401 Unauthorized or 403 Forbidden)"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:
            # OR pattern: server-side errors
            return "Server error"
        case _:
            return "Other"


print(classify_http_error(401))  # Auth error (401 Unauthorized or 403 Forbidden)
print(classify_http_error(503))  # Server error
print(classify_http_error(200))  # Other


# ============================================================
# [block-4] Sequence pattern (tuple / list)
# match works on tuples and lists by structure, not just type.
# This is more powerful than switch: it unpacks values inline.
# ============================================================
def handle_command(command: tuple) -> str:
    match command:
        case ("quit",):
            return "Quitting..."
        case ("go", direction):
            # 'direction' is captured as a variable
            return f"Going {direction}"
        case ("go", direction, speed):
            return f"Going {direction} at speed {speed}"
        case _:
            return f"Unknown command: {command}"


print(handle_command(("quit",)))  # Quitting...
print(handle_command(("go", "north")))  # Going north
print(handle_command(("go", "south", 5)))  # Going south at speed 5
print(handle_command(("fly",)))  # Unknown command: ('fly',)


# ============================================================
# [block-5] Sequence pattern with *rest and *_ (star patterns)
# *rest captures remaining elements as a list.
# *_ discards remaining elements (don't care).
# ============================================================
def summarize_path(parts: list) -> str:
    match parts:
        case []:
            return "Empty path"
        case [only]:
            # Matches al list with exactly one element
            return f"Root segment: {only}"
        case [first, *rest]:
            # Captures first element, rest is a list of remaining
            return f"Base: {first}, rest: {rest}"


print(summarize_path([]))  # Empty path
print(summarize_path(["api"]))  # Root segment: api
print(summarize_path(["api", "vi", "users"]))  # Base: api, rest: ['vi', 'users']


def first_and_last(items: list) -> str:
    match items:
        case [first, *_, last]:
            # *_ discards middle elements (we don't need them)
            return f"First: {first}, Last: {last}"
        case [single]:
            return f"Only one item: {single}"
        case []:
            return "Empty"


print(first_and_last([1, 2, 3, 4, 5]))  # First: 1, Last: 5
print(first_and_last([42]))  # Only one item: 42


# ============================================================
# [block-6] Class pattern  (ClassName(attr=value, ...))
# Matches instances of a class and unpacks attributes.
# __match_args__ allows positional syntax: Point(x, y)
#   instead of: Point(x=x, y=y)
# ============================================================
class Point:
    # __match_args__ defines the order for positional pattern matching
    __match_args__ = ("x", "y")

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y


def classify_point(point: Point) -> str:
    match point:
        case Point(0, 0):
            # Positional syntax works because of __match_args__
            return "Origin"
        case Point(x, 0):
            return f"On X-axis at x={x}"
        case Point(0, y):
            return f"On Y-axis at y={y}"
        case Point(x, y):
            return f"Somewhere at ({x}, {y})"


print(classify_point(Point(0, 0)))  # Origin
print(classify_point(Point(3, 0)))  # On X-axis at x=3
print(classify_point(Point(0, -2)))  # On Y-axis at y=-2
print(classify_point(Point(1, 2)))  # Somewhere at (1, 2)


# ============================================================
# [block-7] Guard clause  (case pattern if condition:)
# A guard adds an extra condition after the pattern.
# The case only matches if BOTH the pattern AND the guard are True.
# Guards are evaluated only when the pattern itself matches.
# ============================================================
def classify_point_with_guard(point: Point):
    match point:
        case Point(x, y) if x == y:
            return f"On diagonal: ({x}, {y})"
        case Point(x, y) if x > 0 and y > 0:
            return f"First quadrant: ({x}, {y})"
        case Point(x, y):
            return f"Other: ({x}, {y})"


print(classify_point_with_guard(Point(3, 3)))  # On diagonal: (3, 3)
print(classify_point_with_guard(Point(2, 5)))  # First quadrant: (2, 5)
print(classify_point_with_guard(Point(-1, 4)))  # Other: (-1, 4)


# ============================================================
# [block-8] Real-world example 1: FastAPI response code routing
# In FastAPI, you often need to handle different HTTP response
# codes from an external API call or a service layer result.
# match is cleaner than a long if/elif chain for this pattern.
# ============================================================

# Simulating a response object (as you'd receive from httpx or requests)
from dataclasses import dataclass


@dataclass
class APIResponse:
    status_code: int
    body: dict
    body: dict


def handle_api_response(response: APIResponse) -> str:
    match response.status_code:
        case 200 | 201:
            return f"Success: {response.body}"
        case 400:
            return f"Bad request sent to external API: {response.body}"
        case 401 | 403:
            return "Auth failure: check API credentials or permissions"
        case 404:
            return "Resource not found on external API"
        case 429:
            return "Rate limited: back off and retry"
        case 500 | 502 | 503:
            return "External API server error: consider circuit breaker"
        case _:
            return f"Unhandled status {response.body}"


# Simulated calls
print(handle_api_response(APIResponse(200, {"id": 1})))
print(handle_api_response(APIResponse(401, {})))
print(handle_api_response(APIResponse(429, {})))


# ============================================================
# [block-9] Real-world example 2: event/action dispatch
# Useful in FastAPI WebSocket handlers, background tasks,
# or command-pattern implementations.
# Sequence pattern makes it easy to dispatch by (action, payload).
# ============================================================
def dispatch_event(event: dict) -> str:
    match event:
        case {"type": "user.created", "user_id": user_id}:
            # Dict pattern: matches dict structure and captures values
            return f"Send welcome email to user {user_id}"
        case {"type": "order.placed", "order_id": order_id, "total": total}:
            return f"Process paymant for order {order_id}, amount: {total}"
        case {"type": "order.cancelled", "order_id": order_id}:
            return f"Refund order {order_id}"
        case {"type": event_type}:
            return f"Unhandled event type: {event_type}"
        case _:
            return "Malformed event"

print(dispatch_event({"type": "user.created", "user_id": 42}))
print(dispatch_event({"type": "order.placed", "order_id": 99, "total": 2980}))
print(dispatch_event({"type": "unknown.event"}))
print(dispatch_event({}))
