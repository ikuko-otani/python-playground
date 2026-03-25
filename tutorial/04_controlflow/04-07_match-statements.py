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
