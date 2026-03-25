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


print(http_method_level("GET"))
print(http_method_level("POST"))
print(http_method_level("PUT"))
print(http_method_level("PATCH"))
print(http_method_level("DELETE"))
print(http_method_level("HEAD"))
