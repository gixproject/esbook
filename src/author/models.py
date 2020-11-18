from db import db
from esbook.models_mixins import IdMixin, CreatedUpdatedMixin, CRUDMixin


class Author(db.Model, IdMixin, CreatedUpdatedMixin, CRUDMixin):
    __tablename__ = "author"

    given_name = db.Column(db.String(length=256), nullable=False, doc="Given name")
    family_name = db.Column(db.String(length=256), nullable=False, doc="Family name")
    middle_name = db.Column(db.String(length=256), doc="Middle name")

    @property
    def full_name(self) -> str:
        """
        Returns formatted author name.
        """
        if self.middle_name:
            full_name = "{} {} {}".format(self.given_name, self.middle_name, self.family_name)
        else:
            full_name = "{} {}".format(self.given_name, self.family_name)

        return full_name
