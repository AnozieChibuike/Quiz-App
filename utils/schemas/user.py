from marshmallow import Schema, fields, validate, EXCLUDE

# Define a Schema with Marshmallow
class UserSchema(Schema):
    fullname = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    bio = fields.Str(default='')
    image_url = fields.Str(default='')
    phone = fields.Str(required=True, validate=validate.Length(min=11))
    is_admin = fields.Boolean(default=False)
    
      
    class Meta:
        unknown = EXCLUDE

class Email(Schema):
    email = fields.Email(required=True)
