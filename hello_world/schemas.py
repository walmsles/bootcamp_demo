new_user = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "object",
    "title": "new user schema",
    "description": "The root schema comprises the entire JSON document.",
    "examples": [{"email": "hello world", "username": "michael", "password": "secret", "confirm_password": "secret", "name": "Michael Walmsley"}],
    "required": ["email", "username", "password", "name"],
    "properties": {
        "email": {
            "$id": "#/properties/email",
            "type": "string",
            "format": "email",
            "title": "User Email Address",
            "examples": ["michael@example.com"],
            "maxLength": 100,
        },
        "username": {
            "$id": "#/properties/username",
            "type": "string",
            "title": "The username",
            "examples": ["michael"],
            "maxLength": 30,
        },
        "password": {
            "$id": "#/properties/password",
            "type": "string",
            "title": "The password",
            "minLength": 6,
            "examples": ["secret"],
            "maxLength": 100,
        },
        "confirm_password": {
            "$id": "#/properties/confirm_password",
            "type": "string",
            "title": "The password",
            "const": {
                "$data": "1/password"
            },
        },
    },
}

