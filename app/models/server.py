__all__ = ["Server"]

import uuid
from tortoise import Model, fields


class Server(Model):
    id = fields.UUIDField(pk=True, default=uuid.uuid4())
    owner = fields.ForeignKeyField("models.User", related_name="linked_servers")
    name = fields.CharField(24, unique=True)
    host = fields.CharField(24, unique=True)
    api_key = fields.CharField(128)
    email = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    modified_at = fields.DatetimeField(auto_now=True)
    is_disabled = fields.BooleanField(default=False)