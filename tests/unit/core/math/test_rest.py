"""Test REST API models."""

import uuid
from typing import Any

import pytest

from wse_exercises.core.math import SimpleCalcTask
from wse_exercises.core.math.rest import SimpleCalcResponse


@pytest.fixture
def request_data() -> dict[str, Any]:
    """Fixture providing request data of division task."""
    return {
        'name': 'multiplication',
        'config': {
            'min_value': 3,
            'max_value': 9,
        },
        'is_rewardable': True,
    }


@pytest.fixture
def response_dto(
    uid: uuid.UUID,
    adding_task_dto: SimpleCalcTask,
) -> SimpleCalcResponse:
    """Fixture providing response DTO of simple calculation task."""
    return SimpleCalcResponse(
        uid=uid,
        task=adding_task_dto,
    )


def test_task_response_roundtrip(
    response_dto: SimpleCalcResponse,
) -> None:
    """Test the simple calculation task response DTO creating."""
    # Dict roundtrip: DTO -> Dict -> DTO
    data = response_dto.to_dict()
    assert response_dto == SimpleCalcResponse.from_dict(data)

    # Json roundtrip: DTO -> Json -> DTO
    json_data = response_dto.to_json()
    assert response_dto == SimpleCalcResponse.from_json(json_data)
