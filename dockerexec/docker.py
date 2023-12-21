from flask import Flask, Blueprint
from flask_restful import Api
from docker import DockerClient

from dockerexec.config import Config

apiv1_bp = Blueprint("apiv1", __name__, url_prefix="/api/v1")
apiv1 = Api(apiv1_bp)

docker = DockerClient(base_url="unix:///var/run/docker.sock")

from dockerexec import resource

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(apiv1_bp)
    return app
