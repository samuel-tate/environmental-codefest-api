from api.app import db


class Issue(db.Model):

    __tablename__ = "issues"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    preview = db.Column(db.String(1024), nullable=False)
    message = db.Column(db.String(8192), nullable=False)
    sources = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return "<User '{}'>".format(self.title)

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "preview": self.preview,
            "message": self.message,
            "sources": self.sources,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
