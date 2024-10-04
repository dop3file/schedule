class BaseCustomError(Exception):
    pass


class DBError(BaseCustomError):
    pass


class UserError(BaseCustomError):
    pass

class CreateUserError(UserError):
    pass


class UserNotFoundError(UserError):
    pass