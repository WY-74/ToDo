from dataclasses import dataclass


@dataclass
class AccessToken:
    get_token: str = "$..access_token"
