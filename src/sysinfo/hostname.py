from platform import node


def get(result):
    result["HOSTNAME"] = node()
