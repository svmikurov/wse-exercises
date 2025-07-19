"""Test DTO."""

import json
from datetime import datetime
from typing import Any

from wse_exercises.core.math.task import SimpleCalcTask


class TestDTOSerialization:
    """Test suite for DTO serialization behavior."""

    def test_json_serialization(
        self,
        created: datetime,
        adding_task_data: dict[str, Any],
    ) -> None:
        """Test JSON serialization roundtrip."""
        # Create original task from fixture
        task = SimpleCalcTask(**adding_task_data)

        # Convert to JSON string
        json_str = task.to_json()

        # Parse JSON back to dictionary
        loaded_data = SimpleCalcTask.from_json(json_str)

        assert loaded_data.config.min_value == 1
        assert loaded_data.config.max_value == 9

        assert loaded_data.conditions.operand_1 == 2
        assert loaded_data.conditions.operand_2 == 3

        assert loaded_data.question.text == '2 + 3'
        assert loaded_data.answer.number == 5

        assert loaded_data.exercise_name == 'adding'

        assert loaded_data.created_at == created

    def test_json_deserialization(
        self,
        created: datetime,
        adding_task_data: dict[str, Any],
    ) -> None:
        """Test JSON deserialization."""
        # Convert to JSON string
        json_str = json.dumps(adding_task_data)

        # Create original task from JSON
        task = SimpleCalcTask.from_json(json_str)

        assert task.config.min_value == 1
        assert task.config.max_value == 9

        assert task.conditions.operand_1 == 2
        assert task.conditions.operand_2 == 3

        assert task.question.text == '2 + 3'
        assert task.answer.number == 5

        assert task.exercise_name == 'adding'

        assert task.created_at == created

    def test_serialization_roundtrips(
        self,
        created: datetime,
        adding_task_data: dict[str, Any],
    ) -> None:
        """Test dictionary conversion roundtrip."""
        # Create original task from fixture
        task = SimpleCalcTask(**adding_task_data)

        # Dict roundtrip
        dict_data = task.to_dict()

        assert SimpleCalcTask(**dict_data) == task

        # JSON roundtrip
        json_data = task.to_json()
        assert SimpleCalcTask.from_json(json_data) == task
