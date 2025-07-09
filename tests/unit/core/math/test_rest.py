"""Test REST API models."""

from typing import Any

import pytest

from wse_exercises.core.math.rest import SimpleCalcRequest


@pytest.fixture
def division_request_data() -> dict[str, Any]:
    """Fixture providing request data of division task."""
    return {
        'name': 'multiplication',
        'config': {
            'min_value': 3,
            'max_value': 9,
        },
    }

task_data = {
    'uid': '4178d9d3-e916-422a-b411-8b2e87cb4939',
    'task': {
        'config': {'min_value': 1, 'max_value': 9},
        'conditions': {'operand_1': 6, 'operand_2': 3},
        'question': {'text': '6 + 3'},
        'answer': {'text': '9'},
        'exercise_name': 'adding',
        'created': '2025-07-08T00:22:49.015256+00:00'},
}


def test_create_simple_calc_request_model(
    division_request_data: dict[str, Any],
) -> None:
    """Test the initialization of model for simple calc request."""
    SimpleCalcRequest.from_dict(division_request_data)
