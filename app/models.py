from app.extensions import funkydb

class Video(funkydb.Model):
    id = funkydb.Column(funkydb.Integer, primary_key=True)
    title = funkydb.Column(funkydb.String(100), nullable=False)
    thumbnail = funkydb.Column(funkydb.String(200), nullable=False)
    file = funkydb.Column(funkydb.String(200), nullable=False)

class Order(funkydb.Model):
    id = funkydb.Column(funkydb.Integer, primary_key=True)
    user = funkydb.Column(funkydb.String(100), nullable=False)
    video_id = funkydb.Column(funkydb.Integer, funkydb.ForeignKey('video.id'), nullable=False)
