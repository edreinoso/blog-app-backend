# general schema for blog post
post_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "content": {"type": "string"},
    },
    "required": ["title", "content"]
}


put_blog_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string", "nullable": True},
        "content": {"type": "string", "nullable": True},
    },
}

post_paginate_schema = {
    "type": "object",
    "properties": {
        "cursor": {"type": "number", "nullable": True},
        "limit": {"type": "number", "nullable": True},
    },
}
