from dataclasses import asdict

from src.controllers.types import (HTTPAuthenticatedRequest, HTTPRequest,
                                   HTTPResponse)
from src.controllers.utils import validate_schema
from src.errors import ValidationError
from src.use_cases import (add_blogpost, edit_blogpost, list_blogposts,
                           remove_blogpost, retrieve_blogpost, retrieve_all_blogposts)

from .blogpost_controller_schema import (post_paginate_schema, post_schema,
                                         put_blog_schema)


def post_paginate(req: HTTPRequest) -> HTTPResponse:
    validate_schema(req.body, post_paginate_schema)

    blogposts, users, has_more = list_blogposts(req.body)

    return HTTPResponse(
        status=200,
        body={
            'blogposts': [asdict(blogpost) for blogpost in blogposts],
            'users': [asdict(user) for user in users],
            'has_more': has_more
        })


def post(req: HTTPRequest) -> HTTPResponse:
    validate_schema(req.body, post_schema)

    print('DEBUGGING: controller/post', req.headers['Userid'])

    blogpost = add_blogpost(req.headers['Userid'], req.body)

    return HTTPResponse(status=201, body=asdict(blogpost))

def get_all_blogs(req: HTTPRequest) -> HTTPResponse:
    blogposts, users = retrieve_all_blogposts()

    print('DEBUGGING: controller/get_all_blogs', req)

    return HTTPResponse(
        status=201, 
        body={
            'blogposts': [asdict(blogpost) for blogpost in blogposts],
            'users': [asdict(user) for user in users]
        }
    )


def get_blog(req: HTTPRequest) -> HTTPResponse:
    if 'id' not in req.args:
        raise ValidationError("You must specify a blog post id.")

    blogpost = retrieve_blogpost(req.args['id'])

    return HTTPResponse(status=200, body=asdict(blogpost))


def put_blog(req: HTTPRequest) -> HTTPResponse:
    if 'id' not in req.args:
        raise ValidationError("You must specify a blog post id.")

    validate_schema(req.body, put_blog_schema)

    blogpost = edit_blogpost(req.user.id, req.args['id'], req.body)

    return HTTPResponse(status=200, body=asdict(blogpost))


def delete_blog(req: HTTPRequest) -> HTTPResponse:
    if 'id' not in req.args:
        raise ValidationError("You must specify a blog post id.")

    remove_blogpost(req.user.id, req.args['id'])

    return HTTPResponse(status=200, body={})
