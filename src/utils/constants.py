from typing import List, Literal

DEFAULT_PASSWORD_LENGTH: Literal[10] = 10
LOWER_CASE_LETTERS: List[str] = [chr(i) for i in range(97, 123)]
UPPER_CASE_LETTERS: List[str] = [chr(i) for i in range(65, 91)]
NUMBERS: List[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
DEFAULT_SPECIAL_CHARS: List[str] = ["*", "-", "_", "@", "#", "!", "=", "-", "+", "?", "$"]
MAX_SHUFFLE_LOOP: Literal[10] = 10
MIN_PASSWORD_LENGTH_FOR_SHUFFLE_LOOP: Literal[8] = 8
