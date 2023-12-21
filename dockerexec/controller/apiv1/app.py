from flask import request

from dockerexec.docker import docker
from dockerexec.utils import jsonify

class DockerController:

    def get_containers_list():
        if request.content_type != "application/json":
            return jsonify(status=415, code=101)
        try:
            docker.ping()
        except:
            return jsonify(status=500, code=102)
        containers = docker.containers.list()
        containers_list = []
        for container in containers:
            containers_list.append(
                {
                    "id" : container.short_id,
                    "name" : container.name
                }
            )
        return {"containers" : containers_list}


    def exec_container(container):
        data = request.get_json()
        if "command" not in data:
            return jsonify(status=400, code=103)
        try:
            container = docker.containers.get(container)
        except:
            return jsonify(status=404, code=104)
        result = container.exec_run(data["command"], demux=True, tty=True)
        return {
            "stdout" : result.output[0].decode("utf8") if result.output[0] is not None else None ,
            "stderr" : result.output[1].decode("utf8") if result.output[1] is not None else None ,
            "exit_code" : result.exit_code
        }
