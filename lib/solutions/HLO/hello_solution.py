from errors.HLO_R1_errors import NotAString

# noinspection PyUnusedLocal
# friend_name = unicode string


def hello(friend_name):
    if not isinstance(friend_name, str):
        raise NotAString(friend_name)
    return "Hello, World!"






