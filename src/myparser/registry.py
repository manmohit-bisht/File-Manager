COMMAND_REGISTRY = {}


def command(name: str, allowed_flags: list[str] = None):
    def decorator(func):
        COMMAND_REGISTRY[name] = {"func": func, "flags": allowed_flags or []}
        return func

    return decorator
