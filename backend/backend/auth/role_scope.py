from enum import Enum


class RoleScope(list, Enum):
    developer = ["me", "items"]
    project_manager = []
    qa_tester = []
    owner = []