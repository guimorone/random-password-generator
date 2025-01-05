from .constants import NO_OPTION_CHOSEN_MSG, PASSWORD_LENGTH_MSG


class NoOptionChosenException(ValueError):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(NO_OPTION_CHOSEN_MSG, *args, **kwargs)


class PasswordLengthException(ValueError):
    def __init__(self, min_length: int, *args, **kwargs) -> None:
        super().__init__(PASSWORD_LENGTH_MSG % min_length, *args, **kwargs)
