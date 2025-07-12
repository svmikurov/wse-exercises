"""Defines library types."""

from typing import TypeVar

from .base.components import Answer, Conditions, Config, Question
from .base.enums import Exercise

AnswerT = TypeVar('AnswerT', bound=Answer)
ConditionsT = TypeVar('ConditionsT', bound=Conditions)
ConfigT = TypeVar('ConfigT', bound=Config)
ExerciseT = TypeVar('ExerciseT', bound=Exercise)
QuestionT = TypeVar('QuestionT', bound=Question)
