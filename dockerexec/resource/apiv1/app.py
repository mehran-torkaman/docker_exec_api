from flask_restful import Resource

from dockerexec.controller.apiv1 import DockerController

class DockerResource(Resource):

    def get(self):
        return DockerController.get_containers_list()

    def post(self, container):
        return DockerController.exec_container(container)
