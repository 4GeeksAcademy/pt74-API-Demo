from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "book"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    author_id = db.Column(
        db.Integer,
        db.ForeignKey("author.id")
    )
    author = db.relationship(
        "Author",
        backref=db.backref(
            "books",
            uselist=True,
        )
    )

    title = db.Column(
        db.Text,
        nullable=False,
    )
    isbn10 = db.Column(
        db.String(32),
        unique=True,
    )
    isbn13 = db.Column(
        db.String(32),
        unique=True,
    )
    cover = db.Column(
        db.String(256)
    )
    have_read = db.Column(
        db.Boolean,
        default=False,
    )
    is_awesome = db.Column(
        db.Boolean,
        default=True,
    )

    def __repr__(self):
        return f"<Book: {self.title}>"


class Author(db.Model):
    __tablename__ = "author"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.String(256),
    )
    # There is a secret "books" property added by
    # the backref of the relationship.  Pretend
    # you can see it and you'll be fine.

    def __repr__(self):
        return f"<Author: {self.name}>"
