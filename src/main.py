import sys
from typing import List
from random import choice, shuffle
from utils.exceptions import NoOptionChosenException, PasswordLengthException
from utils.constants import (
    DEFAULT_PASSWORD_LENGTH,
    LOWER_CASE_LETTERS,
    UPPER_CASE_LETTERS,
    NUMBERS,
    DEFAULT_SPECIAL_CHARS,
)


def generate_random_password(
    password_length: int = DEFAULT_PASSWORD_LENGTH,
    *,
    use_lower_case_letters: bool = True,
    use_upper_case_letters: bool = True,
    use_numbers: bool = True,
    use_special_chars: bool = True,
    special_chars: List[str] = DEFAULT_SPECIAL_CHARS,
) -> str:
    """# Generate Random Password

    ### Args:
        password_length (int, optional): The random password length. Defaults to `DEFAULT_PASSWORD_LENGTH` constant value.
        use_lower_case_letters (bool, optional): If the password must have lower case letters. Defaults to `True`.
        use_upper_case_letters (bool, optional): If the password must have upper case letters. Defaults to `True`.
        use_numbers (bool, optional): If the password must have numbers. Defaults to `True`.
        use_special_chars (bool, optional): If the password must have special characters. Defaults to `True`.
        special_chars (List[str], optional): Special characters list that must be consider. Defaults to `DEFAULT_SPECIAL_CHARS` constant value.

    ### Raises:
        NoOptionChosenException: If none of the following parameters are `True`: `use_lower_case_letters`, `use_upper_case_letters`, `use_numbers`, `use_special_chars`.
        PasswordLengthException: If `password_length` is less than the number of options chosen (`use_lower_case_letters`, `use_upper_case_letters`, `use_numbers`, `use_special_chars`).

    ### Returns:
        str: The random password generated
    """

    min_length: int = 0
    all_chars: List[str] = []

    def check_password_length() -> bool:
        return min_length <= password_length

    def helper(password: str) -> str:
        for _ in range(password_length - min_length):
            password += choice(all_chars)

        l: List[str] = list(password)
        shuffle(l)

        return "".join(l)

    password: str = ""
    if use_lower_case_letters:
        min_length += 1
        password += choice(LOWER_CASE_LETTERS)
        all_chars.extend(LOWER_CASE_LETTERS)
    if use_upper_case_letters:
        min_length += 1
        password += choice(UPPER_CASE_LETTERS)
        all_chars.extend(UPPER_CASE_LETTERS)
    if use_numbers:
        min_length += 1
        password += choice(NUMBERS)
        all_chars.extend(NUMBERS)
    if use_special_chars:
        min_length += 1
        password += choice(special_chars)
        all_chars.extend(special_chars)

    if min_length <= 0:
        raise NoOptionChosenException()

    if not check_password_length():
        raise PasswordLengthException(min_length)

    return helper(password)


if __name__ == "__main__":
    password_length: int = int(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PASSWORD_LENGTH
    print("Password:", generate_random_password(password_length))
