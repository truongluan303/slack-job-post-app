import os


class OSEnvKeys:
    """
    Containing the names of the OS environment keys
    """

    SLACK_API_TOKEN = "SLACK_API_TOKEN"

    @classmethod
    def to_list(cls):
        """Return a list of the OS environment keys"""
        condition = lambda x: not callable(getattr(cls, x)) and not x.startswith("__")
        return [getattr(cls, attr) for attr in dir(cls) if condition(attr)]


# Create variables for each OS environment keys
# Default to `None` if the key does not exist
for env_key in OSEnvKeys.to_list():
    globals()[env_key.upper()] = os.environ.get(env_key, None)
