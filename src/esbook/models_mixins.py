import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from db import db


class IdMixin:
    """
    Mixin for unique UUID primary key.
    """

    id = db.Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)


class CreatedUpdatedMixin:
    """
    Mixin for timestamp values.
    """

    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow()
    )


class CRUDMixin:
    """
    CRUD mixin for quick actions with models.
    """

    def save(self, commit=True):
        db.session.add(self)
        return commit and db.session.commit()

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()

    @classmethod
    def get_or_create(cls, **kwargs):
        instance = cls.query.filter_by(**kwargs).first()

        if not instance:
            instance = cls(**kwargs)
            instance.save()

        return instance
