"""Test DTO."""

import json
from datetime import datetime, timezone
from typing import Any

import pytest

from wse_exercises.core.mathem.task import SimpleMathTask


@pytest.fixture
def serialized_task() -> dict[str, Any]:
    """Fixture providing data for serialization tests.

    :return: Complete task data with timestamp
    :rtype: dict[str, Any]
    """
    return {
        'config': {'min_value': 1, 'max_value': 9},
        'conditions': {'operand_1': 2, 'operand_2': 3},
        'question': {'text': '2 + 3'},
        'answer': {'text': '5'},
        'exercise_name': 'adding',
        'created': '2025-05-21T18:00:00Z',
        'error_msg': '',
    }


class TestDTOSerialization:
    """Test suite for DTO serialization behavior."""

    def test_json_serialization(self, serialized_task: dict[str, Any]) -> None:
        """Test JSON serialization roundtrip.

        :param dict[str, Any] serialized_task: Task data fixture
        :rtype: None
        """
        # Create original task from fixture
        task = SimpleMathTask(**serialized_task)

        # Convert to JSON string
        json_str = task.model_dump_json()

        # Parse JSON back to dictionary
        loaded_data = json.loads(json_str)

        assert loaded_data['config']['min_value'] == 1
        assert loaded_data['config']['max_value'] == 9

        assert loaded_data['conditions']['operand_1'] == 2
        assert loaded_data['conditions']['operand_2'] == 3

        assert loaded_data['question']['text'] == '2 + 3'
        assert loaded_data['answer']['text'] == '5'

        assert loaded_data['exercise_name'] == 'adding'

        assert loaded_data['created'] == '2025-05-21T18:00:00Z'

    def test_json_deserialization(
        self, serialized_task: dict[str, Any]
    ) -> None:
        """Test JSON deserialization.

        :param dict[str, Any] serialized_task: Task data fixture
        :rtype: None
        """
        # Convert to JSON string
        json_str = json.dumps(serialized_task)

        # Create original task from JSON
        task = SimpleMathTask.model_validate_json(json_str)

        assert task.config.min_value == 1
        assert task.config.max_value == 9

        assert task.conditions.operand_1 == 2
        assert task.conditions.operand_2 == 3

        assert task.question.text == '2 + 3'
        assert task.answer.text == '5'

        assert task.exercise_name == 'adding'

        expected_time = datetime(2025, 5, 21, 18, 0, tzinfo=timezone.utc)
        assert task.created == expected_time

    def test_serialization_roundtrips(
        self, serialized_task: dict[str, Any]
    ) -> None:
        """Test dictionary conversion roundtrip.

        :param dict[str, Any] serialized_task: Task data fixture
        :rtype: None
        """
        # Create original task from fixture
        task = SimpleMathTask(**serialized_task)

        # Dict roundtrip
        dict_data = task.model_dump()
        assert SimpleMathTask(**dict_data) == task

        # JSON roundtrip
        json_data = task.model_dump_json()
        assert SimpleMathTask.model_validate_json(json_data) == task

        # Comparison of structures - convert both to comparable forms
        json_dict = json.loads(json_data)
        dict_data_serializable = task.model_dump(mode='json')

        assert json_dict == dict_data_serializable
        assert dict_data_serializable == serialized_task
