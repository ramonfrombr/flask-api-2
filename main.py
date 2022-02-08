from flask import Flask, request, jsonify
from flask_restful import Api, Resource, marshal, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


resource_fields = {
    'id': fields.Integer,
    'nome': fields.String,
    'visualizacoes': fields.Integer,
    'likes': fields.Integer
}



class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    visualizacoes = db.Column(db.Integer)
    likes = db.Column(db.Integer)

    def __repr__(self):
        return f"Video(nome={self.nome}, visualizacoes={self.visualizacoes}, likes={self.likes})"




video_post_args = reqparse.RequestParser()
video_post_args.add_argument("nome", type=str, help="Nome do vídeo", required=True)
video_post_args.add_argument("visualizacoes", type=int, help="Visualizações do vídeo", required=True)
video_post_args.add_argument("likes", type=int, help="Likes do vídeo", required=True)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("nome", type=str, help="Nome do vídeo")
video_put_args.add_argument("visualizacoes", type=int, help="Visualizações do vídeo")
video_put_args.add_argument("likes", type=int, help="Likes do vídeo")



class VideoResource(Resource):

    @marshal_with(resource_fields)
    def get(self, video_id):
        
        video = Video.query.get(video_id)
        
        if not video:
            abort(404, message="Não conseguimos encontrar o vídeo com o id informado.")
        
        return video

    @marshal_with(resource_fields)
    def put(self, video_id):

        video = Video.query.get(video_id)
        if not video:
            abort(404, message="Não conseguimos encontrar o vídeo com o id informado.")
        
        args = video_post_args.parse_args()
        if "nome" in args:
            video.nome = args['nome']
        if "visualizacoes" in args:
            video.visualizacoes = args['visualizacoes']
        if "likes" in args:
            video.likes = args['likes']

        db.session.add(video)
        db.session.commit()

        return video

    @marshal_with(resource_fields)
    def delete(self, video_id):


        video = Video.query.get(video_id)

        if not video:
            abort(404, message="Não existe um vídeo com o id informado.")

        db.session.delete(video)
        db.session.commit()

        return video

class VideosResource(Resource):

    @marshal_with(resource_fields)
    def get(self):

        videos = Video.query.all()
        return videos
    
    @marshal_with(resource_fields)
    def post(self):

        args = video_post_args.parse_args()
        video = Video(**args)

        db.session.add(video)
        db.session.commit()
        return video
      


api.add_resource(VideoResource, '/videos/<int:video_id>')
api.add_resource(VideosResource, '/videos')


if __name__ == "__main__":
    app.run(debug=True)

