"""Test DTO."""

import json
from datetime import datetime
from typing import Any

from wse_exercises.core.math.task import SimpleMathTask


class TestDTOSerialization:
    """Test suite for DTO serialization behavior."""

    def test_json_serialization(
        self,
        created: datetime,
        simple_math_task_dict: dict[str, Any],
    ) -> None:
        """Test JSON serialization roundtrip.

        :param dict[str, Any] serialized_task: Task data fixture
        :rtype: None
        """
        # Create original task from fixture
        task = SimpleMathTask(**simple_math_task_dict)

        # Convert to JSON string
        json_str = task.json()

        # Parse JSON back to dictionary
        loaded_data = SimpleMathTask.parse_raw(json_str)

        assert loaded_data.config.min_value == 1
        assert loaded_data.config.max_value == 9

        assert loaded_data.conditions.operand_1 == 2
        assert loaded_data.conditions.operand_2 == 3

        assert loaded_data.question.text == '2 + 3'
        assert loaded_data.answer.text == '5'

        assert loaded_data.exercise_name == 'adding'

        assert loaded_data.created == created

    def test_json_deserialization(
        self,
        created: datetime,
        simple_math_task_dict: dict[str, Any],
    ) -> None:
        """Test JSON deserialization.

        :param dict[str, Any] serialized_task: Task data fixture
        :rtype: None
        """
        # Convert to JSON string
        json_str = json.dumps(simple_math_task_dict)

        # Create original task from JSON
        task = SimpleMathTask.parse_raw(json_str)

        assert task.config.min_value == 1
        assert task.config.max_value == 9

        assert task.conditions.operand_1 == 2
        assert task.conditions.operand_2 == 3

        assert task.question.text == '2 + 3'
        assert task.answer.text == '5'

        assert task.exercise_name == 'adding'

        assert task.created == created

    def test_serialization_roundtrips(
        self,
        created: datetime,
        simple_math_task_dict: dict[str, Any],
    ) -> None:
        """Test dictionary conversion roundtrip.

        :param dict[str, Any] serialized_task: Task data fixture
        :rtype: None
        """
        # Create original task from fixture
        task = SimpleMathTask(**simple_math_task_dict)

        # Dict roundtrip
        dict_data = task.dict()

        assert SimpleMathTask(**dict_data) == task

        # JSON roundtrip
        json_data = task.json()
        assert SimpleMathTask.parse_raw(json_data) == task
