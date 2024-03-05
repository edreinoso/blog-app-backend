import logging
import sys
import traceback
from typing import Callable, Union

from flask import Response as FlaskResponse
from flask import current_app, jsonify
from flask import request as flask_req
from flask_login import current_user
from src.constants import MSG_UNKNOWN_ERROR
from src.controllers.types import (HTTPAuthenticatedRequest, HTTPRequest,
                                   HTTPResponse)
from src.errors import AuthorizationError, ValidationError
from src.router.middleware.auth import flask_to_internal_user


def parse_flask_request() -> HTTPRequest:
    body: dict
    try:
        body = flask_req.get_json() if flask_req.is_json else {}
    except Exception:
        body = {}

    req_data = {
        "resource": flask_req.path,
        "method": flask_req.method,
        "body": body,
        "args": {**flask_req.args, **flask_req.view_args, **flask_req.form},
        "headers": dict(flask_req.headers)
    }
    
    print('DEBUGGING/utils: ',current_user, current_user.is_authenticated)
    
    return (
        HTTPRequest(**req_data)

        # Commenting until there is a way of fixing this issue with react
        # HTTPAuthenticatedRequest(**req_data, user=flask_to_internal_user())
        # if current_user is not None and current_user.is_authenticated
        # else HTTPRequest(**req_data)
        
        )


def run_flask_controller(
    controller: Callable[[HTTPRequest], HTTPResponse],
) -> Union[FlaskResponse, tuple[FlaskResponse, int]]:

    try:
        request = parse_flask_request()
        response: HTTPResponse = controller(request)
        return jsonify(data=response.body), response.status

    except ValidationError as e:
        return jsonify(errors=[str(e)]), 400

    except AuthorizationError as e:
        return jsonify(errors=[str(e)]), 401

    except Exception as e:
        logging.log(
            logging.ERROR,
            f'{flask_req.method} {flask_req.path} - {str(e)}\n{format_exception(e)}'
        )

        if current_app.debug:
            raise e

        return jsonify(errors=[MSG_UNKNOWN_ERROR], exc=str(e)), 500


def format_exception(e: Exception):
    # from https://stackoverflow.com/questions/6086976/how-to-get-a-complete-exception-stack-trace-in-python
    exception_list = traceback.format_stack()
    exception_list = exception_list[:-2]
    exception_list.extend(traceback.format_tb(sys.exc_info()[2]))
    exception_list.extend(traceback.format_exception_only(
        sys.exc_info()[0], sys.exc_info()[1]))

    exception_str = "Traceback (most recent call last):\n"
    exception_str += "".join(exception_list)
    # Removing the last \n
    exception_str = exception_str[:-1]

    return exception_str
