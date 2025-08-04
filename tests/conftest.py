"""Defines configuration for Pytest."""

import json
import uuid
from datetime import datetime, timezone
from typing import Any

import pytest

from wse_exercises.core.math.base.components import (
    CalcAnswer,
    CalcConditions,
    CalcConfig,
    CalcQuestion,
)
from wse_exercises.core.math.enums import MathEnum
from wse_exercises.core.math.task import CalcTask


@pytest.fixture
def created() -> datetime:
    """Fixture providing datetime."""
    return datetime.now(timezone.utc)


@pytest.fixture
def uid() -> uuid.UUID:
    """Fixture providing the uid."""
    return uuid.uuid4()


@pytest.fixture
def adding_task_dto(created: datetime) -> CalcTask:
    """Fixture providing simple math task DTO."""
    return CalcTask(
        config=CalcConfig(min_value=1, max_value=9, ttl=3600),
        conditions=CalcConditions(operand_1=2, operand_2=3),
        question=CalcQuestion(text='2 + 3'),
        answer=CalcAnswer(number=5),
        exercise_name=MathEnum.ADDING,
        created_at=created,
    )


@pytest.fixture
def adding_task_data(created: datetime) -> dict[str, Any]:
    """Fixture providing data for serialization tests."""
    return {
        'config': {'ttl': 3600, 'min_value': 1, 'max_value': 9},
        'conditions': {'operand_1': 2, 'operand_2': 3, 'time': 60},
        'question': {'text': '2 + 3'},
        'answer': {'number': 5},
        'exercise_name': MathEnum.ADDING,
        'created_at': created.isoformat(),
    }


@pytest.fixture
def adding_task_json(adding_task_data: dict[str, Any]) -> str:
    """Fixture providing data for serialization tests."""
    json_str = json.dumps(adding_task_data)
    return json_str
