"""Defines base exercise class."""

from typing import Generic, TypeVar

from pydantic import BaseModel

from wse_exercises.core.math.enums import Exercises

ConfigT = TypeVar('ConfigT', bound='ExerciseConfig')


class ExerciseConfig(BaseModel):
    """Exercise base config."""


class TaskRequest(BaseModel, Generic[ConfigT]):
    """Request an exercise with a given configuration.

    :param Exercises name: Exercise name.
    :param ExerciseConfig config: Exercise configuration.
    """

    name: Exercises
    config: ConfigT
