import logging

import src.controllers.users.users_controller as UsersController
from flask import Blueprint, jsonify
from flask_cors import CORS
from flask_login import login_required, login_user, logout_user
from src.constants import MSG_UNKNOWN_ERROR
from src.errors import AuthorizationError, ValidationError
from src.router.middleware.auth import FlaskUser
from src.router.utils import (format_exception, parse_flask_request,
                              run_flask_controller)

blueprint_users = Blueprint('users', __name__, url_prefix='/users')
CORS(blueprint_users)


@blueprint_users.route('/login', methods=['POST'])
def route_users_login():
    # NOTE(andrea): this is an antipattern but it is the only
    # scenario in which we do this in order to take advantage
    # of the Flask-Login plugin.
    request = parse_flask_request()

    try:
        response = UsersController.post_login(request)
        user = FlaskUser(
            **response.body,
            is_active=True,
            is_anonymous=False,
            is_authenticated=True)
        login_user(user)
        return jsonify(data=response.body), response.status

    except ValidationError as e:
        return jsonify(errors=[str(e)]), 400

    except AuthorizationError as e:
        return jsonify(errors=[str(e)]), 401

    except Exception as e:
        logging.log(
            logging.ERROR,
            f'POST /users/login - {str(e)}\n{format_exception(e)}'
        )
        return jsonify(errors=[MSG_UNKNOWN_ERROR], exc=str(e)), 500


@login_required
@blueprint_users.route('/logout', methods=['POST'])
def route_users_logout():
    logout_user()
    return 200


@blueprint_users.route('/', methods=['POST'])
def route_users():
    return run_flask_controller(UsersController.post)
