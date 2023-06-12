from enum import Enum


class RoleScope(str, Enum):
    developer = ['me', 'bug', 'project', 'comment']
    project_manager = ['me', 'bug', 'project', 'comment', 'user']
    admin = ['me', 'bug', 'project', 'comment', 'user', 'role', 'project_manager', 'developer', 'owner', 'admin']
    qa_tester = ['me', 'bug', 'project', 'comment']


if __name__ == "__main__":
    role = 'developer'
    print(eval(f'RoleScope.{role}.value'))