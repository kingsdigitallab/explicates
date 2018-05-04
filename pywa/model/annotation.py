# -*- coding: utf8 -*-

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy import Integer, Text, Unicode
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from pywa.core import db
from pywa.model import make_timestamp, make_uuid
from pywa.model.base import BaseDomainObject
from pywa.model.collection import Collection


class Annotation(db.Model, BaseDomainObject):
    """An annotation"""

    __tablename__ = 'annotation'

    #: The Annotation ID
    id = Column(Integer, primary_key=True)

    #: The IRI path segement appended to the Annotation IRI.
    slug = Column(Unicode(), unique=True, default=unicode(make_uuid()))

    #: The relationship between the Annotation and its Body.
    body = Column(JSONB, nullable=False)

    #: The relationship between the Annotation and its Target.
    target = Column(JSONB, nullable=False)

    #: The time at which the Annotation was created.
    created = Column(Text, default=make_timestamp)

    #: The agent responsible for creating the Annotation.
    creator = Column(JSONB)

    #: The time at which the Annotation was modified, after creation.
    modified = Column(Text)

    #: The relationship between the Annotation and the Style.
    stylesheet = Column(JSONB)

    #: The related Collection ID.
    collection_id = Column(Integer, ForeignKey('collection.id'),
                           nullable=False)

    #: The related Collection.
    collection = relationship(Collection)