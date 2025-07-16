VALID_TOKENS = {
    "read-token": "read",
    "write-token": "write"
}

def authorize(token):
    if token is None:
        return False
    return token in VALID_TOKENS
