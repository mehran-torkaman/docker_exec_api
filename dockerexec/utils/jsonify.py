from flask import current_app

DBG_MSG = {
    "100" : "OK",
    "101" : "Unsupported Media Type.",
    "102" : "Docker Host Is NOT Available.",
    "103" : "Command Not In Request.",
    "104" : "Container Not Found."
}

def jsonify(state={}, status=200, code=100):
    data = state
    if current_app.debug:
        data["message"] = DBG_MSG[str(code)]
    data["code"] = code
    return data, status
