from enum import Enum


class VimError(Enum):
    SUCCESS = 0
    SUCCESS_MODE_ALREADY_SET = 1
    ERROR_MODE_ADJUSTMENT_SKIPPED = 2
