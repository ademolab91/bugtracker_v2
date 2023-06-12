from enum import Enum


class Tags(str, Enum):
    """ A class that defines the tags for the API """
    users = "users"
    auth = "auth"
    api = "api"