from marshmallow import Schema, fields


class UserSchema(Schema):
    login = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)


class NewUserSchema(Schema):
    name = fields.Str(required=True)
    login = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
