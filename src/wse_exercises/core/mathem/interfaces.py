"""Defines protocol for Simple math exercise interface."""
from typing import Protocol

from wse_exercises.base.interfaces import ITask

from .task import (
    MathTaskConditions,
    MathTaskConfig,
    MathTextTaskAnswer,
    MathTextTaskQuestion,
)


class ISimpleMathTask(
    ITask[
        MathTaskConfig,
        MathTaskConditions,
        MathTextTaskQuestion,
        MathTextTaskAnswer,
    ],
    Protocol,
):
    """Protocol for Simple math exercise interface."""
