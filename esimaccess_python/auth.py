import httpx


class AuthError(Exception):
    """Custom exception for authentication errors."""
    pass


def authenticate(api_key: str) -> httpx.Client:
    """
    Authenticates using the provided API key and returns an authenticated HTTP client.

    :param api_key: The API key (AccessCode) used for authentication.
    :return: An authenticated httpx client with the API key in the headers.
    """
    if not api_key:
        raise AuthError("API key is required for authentication")

    headers = {
        "Authorization": f"RT-AccessCode {api_key}"
    }
    client = httpx.Client(headers=headers)
    return client
