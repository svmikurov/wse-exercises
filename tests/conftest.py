"""Defines configuration for Pytest."""

import json
import uuid
from datetime import datetime, timezone
from typing import Any

import pytest

from wse_exercises.core.math.base.components import (
    SimpleCalcAnswer,
    SimpleCalcConditions,
    SimpleCalcConfig,
    SimpleCalcQuestion,
)
from wse_exercises.core.math.enums import MathExercise
from wse_exercises.core.math.task import SimpleCalcTask


@pytest.fixture
def created() -> datetime:
    """Fixture providing datetime."""
    return datetime.now(timezone.utc)


@pytest.fixture
def uid() -> uuid.UUID:
    """Fixture providing the uid."""
    return uuid.uuid4()


@pytest.fixture
def adding_task_dto(created: datetime) -> SimpleCalcTask:
    """Fixture providing simple math task DTO."""
    return SimpleCalcTask(
        config=SimpleCalcConfig(min_value=1, max_value=9),
        conditions=SimpleCalcConditions(operand_1=2, operand_2=3),
        question=SimpleCalcQuestion(text='2 + 3'),
        answer=SimpleCalcAnswer(text='5'),
        exercise_name=MathExercise.ADDING,
        created=created,
    )


@pytest.fixture
def adding_task_data(created: datetime) -> dict[str, Any]:
    """Fixture providing data for serialization tests."""
    return {
        'config': {'min_value': 1, 'max_value': 9},
        'conditions': {'operand_1': 2, 'operand_2': 3},
        'question': {'text': '2 + 3'},
        'answer': {'text': '5'},
        'exercise_name': MathExercise.ADDING,
        'created': created.isoformat(),
    }


@pytest.fixture
def adding_task_json(adding_task_data: dict[str, Any]) -> str:
    """Fixture providing data for serialization tests."""
    json_str = json.dumps(adding_task_data)
    return json_str
