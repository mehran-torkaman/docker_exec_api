from os import environ

class Config:

    ######################### Global Configration #########################

    ENV = environ.get("DOCKER_EXEC_ENV", "production")

    TESTING = int(environ.get("DOCKER_EXEC_TESTING", "0"))

    DEBUG = int(environ.get("DOCKER_EXEC_DEBUG", "0"))

    JSONIFY_PRETTYPRINT_REGULAR = True
