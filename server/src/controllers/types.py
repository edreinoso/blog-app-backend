from dataclasses import dataclass
from typing import Optional

from src.entities.user import User


@dataclass(frozen=True, eq=True)
class HTTPRequest:
    resource: str
    method: str
    body: dict
    args: dict
    headers: dict


@dataclass(frozen=True, eq=True)
class HTTPAuthenticatedRequest(HTTPRequest):
    user: User


@dataclass(frozen=True, eq=True)
class HTTPResponse:
    status: int
    body: Optional[object]
