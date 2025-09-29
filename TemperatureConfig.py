from enum import Enum
from typing import Literal


class TempMode(Enum):
    LOW = 'low'
    HIGH = 'high'


# 默认低温
_mode: TempMode = TempMode.LOW


def set_mode(mode: TempMode) -> None:
    global _mode
    _mode = mode


def set_low() -> None:
    set_mode(TempMode.LOW)


def set_high() -> None:
    set_mode(TempMode.HIGH)


def get_mode() -> TempMode:
    return _mode


def is_low() -> bool:
    return _mode == TempMode.LOW


def is_high() -> bool:
    return _mode == TempMode.HIGH

