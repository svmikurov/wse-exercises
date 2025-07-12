"""Defines pydantic v1 models for REST API."""

from typing import Any, Generic, TypeVar

from wse_exercises.types import AnswerT, ConfigT, ExerciseT

from .model import BaseShema
from .task import Task

TaskT = TypeVar('TaskT', bound=Task[Any, Any, Any, Any, Any])


class TaskRequest(BaseShema, Generic[ExerciseT, ConfigT]):
    """Model for request the task.

    :param Exercise name: Exercise name.
    :param ExerciseConfig config: Exercise configuration.
    """

    name: ExerciseT
    config: ConfigT


class TaskResponse(BaseShema, Generic[TaskT]):
    """Response model with crated task.

    :param str uid: The unique identifier of task.
    :param TaskT task: Created task.
    """

    uid: str
    task: TaskT


class HandleAnswer(BaseShema, Generic[AnswerT]):
    """Model for request the answer handling.

    :param str uid: The unique identifier of task.
    :param AnswerT answer: Answer to handle.
    :param bool is_rewardable: Is there a reward for the correct answer?
    """

    uid: str
    answer: AnswerT
    is_rewardable: bool = False
