class BaseCustomError(Exception):
    pass


class DBError(BaseCustomError):
    pass


class UserError(BaseCustomError):
    pass


class CreateUserError(UserError):
    pass


class GroupError(BaseCustomError):
    pass


class GroupNotFoundError(GroupError):
    pass


class LessonError(BaseCustomError):
    pass


class UserNotFoundError(UserError):
    pass