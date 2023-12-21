from dockerexec.docker import apiv1 as api
from dockerexec.resource.apiv1.app import DockerResource

api.add_resource(
    DockerResource,
    "/containers",
    methods=["GET"],
    endpoint="containers"
)

api.add_resource(
    DockerResource,
    "/containers/<container>/exec",
    methods=["POST"],
    endpoint="container"
)
