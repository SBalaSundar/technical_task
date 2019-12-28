from flask import Flask
from flask_restful import Api
from process_data import Video


app = Flask(__name__)
api = Api(app)

api.add_resource(Video, "/api/view_count")

app.run(debug=True)

