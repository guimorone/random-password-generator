from typing import List

# ---------------------- Configurations ----------------------
DEFAULT_PASSWORD_LENGTH: int = 20
LOWER_CASE_LETTERS: List[str] = [chr(i) for i in range(97, 123)]
UPPER_CASE_LETTERS: List[str] = [chr(i) for i in range(65, 91)]
NUMBERS: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DEFAULT_SPECIAL_CHARS: List[str] = ["*", "&", "%", "-", "_", "@", "#", "!", "=", "-", "+", "?", "$"]

# -------------------- Exception Messages --------------------
NO_OPTION_CHOSEN_MSG: str = (
    "At least one of the following parameters must be True: `use_lower_case_letters`, `use_upper_case_letters`, `use_numbers`, `use_special_chars`!"
)
PASSWORD_LENGTH_MSG: str = "Password's length must be %d character(s) or more!"
