from app import db


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
        db.String(64), 
        nullable=False
    )

    email = db.Column(
        db.Text, 
        unique=True, 
        nullable=False
    )

    created_by = db.Column(
        db.DateTime, 
        nullable=False
    )


    # friend_ids
    # server_ids
    # channel_ids


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

    created_by = db.Column(
        db.DateTime, 
        nullable=False
    )


    # user_ids
    # channel_ids


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

    created_by = db.Column(
        db.DateTime, 
        nullable=False
    )


    # user_ids


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
        nullable=False
    )


    # sender_id
    # channel_id
