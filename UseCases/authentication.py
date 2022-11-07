def check_roles(roles_list: tuple[str], role: str):
    for x in roles_list:
        if role == x:
            return roles_list.index(x)


def is_authenticated(request_role, role):
    roles = ('', 'editor', 'admin', 'super')

    role = check_roles(roles, role) if role else 0
    request_role = check_roles(roles, request_role) if request_role else 0
    print(role, request_role)

    if role >= request_role:
        return True

    else:
        return False
        print(role, request_role)


if __name__ == "__main__":
    print(is_authenticated('admin', 'editor'))
