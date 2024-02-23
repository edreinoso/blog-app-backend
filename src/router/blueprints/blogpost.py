import src.controllers.blogpost.blogpost_controller as BlogPostController
from flask import Blueprint, request
from flask_cors import CORS
from flask_login import current_user, login_required
from src.router.utils import run_flask_controller

blueprint_blogpost = Blueprint('blogposts', __name__, url_prefix='/blogposts')
CORS(blueprint_blogpost)


@login_required
@blueprint_blogpost.route('/', methods=['POST'])
def route_post_blog():
    return run_flask_controller(BlogPostController.post)


@blueprint_blogpost.route('/', methods=['DELETE', 'GET'])
def route_get_delete_blog():
    if request.method == 'DELETE':
        if not current_user.is_authenticated:
            return 401
        return run_flask_controller(BlogPostController.delete_blog)

    if request.method == 'GET':
        return run_flask_controller(BlogPostController.get_blog)

@blueprint_blogpost.route('/all', methods=['GET'])
def route_get_all_blogs():
    return run_flask_controller(BlogPostController.get_all_blogs)

@login_required
@blueprint_blogpost.route('/', methods=['PUT'])
def route_put_blog():
    return run_flask_controller(BlogPostController.put_blog)


@blueprint_blogpost.route('/paginate', methods=['POST'])
def route_post_paginate():
    return run_flask_controller(BlogPostController.post_paginate)
