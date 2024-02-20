from dataclasses import asdict

from src.controllers.types import HTTPRequest, HTTPResponse
from src.controllers.utils import validate_schema
from src.use_cases import login, signup

from .users_controller_schema import post_login_schema, post_schema


def post_login(req: HTTPRequest) -> HTTPResponse:
    validate_schema(req.body, post_login_schema)
    user = login(req.body['email'], req.body['password'])
    return HTTPResponse(status=200, body=asdict(user))


def post(req: HTTPRequest) -> HTTPResponse:
    validate_schema(req.body, post_schema)
    user = signup(req.body)
    return HTTPResponse(status=200, body=asdict(user))
