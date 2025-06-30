"""Defines configuration for Pytest."""

import json
from datetime import datetime
from typing import Any

import pytest

from wse_exercises.core.mathem.enums import Exercises
from wse_exercises.core.mathem.task import (
    MathTaskConditions,
    MathTaskConfig,
    MathTextAnswer,
    MathTextQuestion,
    SimpleMathTask,
)


@pytest.fixture(scope='package')
def created() -> datetime:
    """Fixture providing datetime."""
    return datetime.now()


@pytest.fixture
def simple_math_task(
    created: datetime,
) -> SimpleMathTask:
    """Fixture providing simple math task DTO."""
    return SimpleMathTask(
        config=MathTaskConfig(min_value=1, max_value=9),
        conditions=MathTaskConditions(operand_1=2, operand_2=3),
        question=MathTextQuestion(text='2 + 3'),
        answer=MathTextAnswer(text='5'),
        exercise_name=Exercises.ADDING,
        created=created,
        error_msg='',
    )


@pytest.fixture
def simple_math_task_dict(
    created: datetime,
) -> dict[str, Any]:
    """Fixture providing data for serialization tests.

    :return: Complete task data with timestamp
    :rtype: dict[str, Any]
    """
    return {
        'config': {'min_value': 1, 'max_value': 9},
        'conditions': {'operand_1': 2, 'operand_2': 3},
        'question': {'text': '2 + 3'},
        'answer': {'text': '5'},
        'exercise_name': Exercises.ADDING,
        'created': created.isoformat(),
        'error_msg': '',
    }


@pytest.fixture
def simple_math_task_json(
    simple_math_task_dict: dict[str, Any],
) -> str:
    """Fixture providing data for serialization tests."""
    json_str = json.dumps(simple_math_task_dict)
    return json_str
