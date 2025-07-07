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


def test_create_simple_calc_request_model(
    division_request_data: dict[str, Any],
) -> None:
    """Test the initialization of model for simple calc request."""
    SimpleCalcRequest.from_dict(division_request_data)
