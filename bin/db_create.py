#!/usr/bin/env python

from alembic.config import Config
from alembic import command

from explicates.core import db, create_app
from explicates.model.collection import Collection


app = create_app()


def db_create():
    """Create the db"""
    with app.app_context():
        db.create_all()
        alembic_cfg = Config("../alembic.ini")
        command.stamp(alembic_cfg, "head")

        # Annotation servers must provide at least one container
        collection = Collection(id="default", label="Default container")
        db.session.add(collection)
        db.session.commit()


if __name__ == '__main__':
    db_create()
