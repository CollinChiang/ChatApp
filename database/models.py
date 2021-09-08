from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(32),
        unique=True,
        nullable=False
    )

    password = db.Column(
        db.String(102),
        nullable=False
    )

    friend_ids = db.Column(
        db.Text,
        default=json.dumps(""),
        nullable=False
    )

    server_ids = db.Column(
        db.Text,
        default=json.dumps(""),
        nullable=False
    )

    channel_ids = db.Column(
        db.Text,
        default=json.dumps(""),
        nullable=False
    )

    """
    email = db.Column(
        db.Text, 
        unique=True, 
        nullable=False
    )
    """

    created_by = db.Column(
        db.DateTime,
        default=datetime.now
    )


class Server(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(32),
        unique=True,
        nullable=False
    )

    user_ids = db.Column(
        db.Text,
        default=json.dumps(""),
        nullable=False
    )

    channel_ids = db.Column(
        db.Text,
        default=json.dumps(""),
        nullable=False
    )

    created_by = db.Column(
        db.DateTime,
        default=datetime.now
    )


class Channel(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(32),
        unique=True,
        nullable=False
    )

    user_ids = db.Column(
        db.Text,
        default=json.dumps(""),
        nullable=False
    )

    is_server = db.Column(
        db.Boolean,
        nullable=False
    )

    created_by = db.Column(
        db.DateTime,
        default=datetime.now
    )


class Message(db.Model):
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    user_id = db.Column(
        db.Integer,
        nullable=False
    )

    channel_id = db.Column(
        db.Integer,
        nullable=False
    )

    content = db.Column(
        db.Text,
        nullable=False
    )

    created_by = db.Column(
        db.DateTime,
        default=datetime.now
    )