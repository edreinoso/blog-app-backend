post_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"},
        # TODO: we expect base64 encoded, we should validate the format
        "image": {"type": "string", "nullable": True},
        "first_name": {"type": "string"},
        "last_name": {"type": "string"},
    }
}


post_login_schema = {
    "type": "object",
    "properties": {
        "email": {"type": "string"},
        "password": {"type": "string"}
    }
}
