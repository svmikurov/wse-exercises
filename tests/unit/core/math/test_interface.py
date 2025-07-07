"""Defines tests for base class for tasks."""

from typing import Any

from wse_exercises.core.math.task import SimpleMathTask


class TestPublicInterface:
    """Test API."""

    def test_from_dict(
        self,
        adding_task_dto: SimpleMathTask,
        adding_task_data: dict[str, Any],
    ) -> None:
        """Test the `from_dict()` method."""
        task = SimpleMathTask.from_dict(adding_task_data)
        assert adding_task_dto == task

    def test_from_json(
        self,
        adding_task_dto: SimpleMathTask,
        adding_task_json: str,
    ) -> None:
        """Test the `from_json()` method."""
        task = SimpleMathTask.from_json(adding_task_json)
        assert adding_task_dto == task

    def test_to_dict(
        self,
        adding_task_dto: SimpleMathTask,
        adding_task_data: dict[str, Any],
    ) -> None:
        """Test the `to_dict()` method."""
        dict_data = adding_task_dto.to_dict()
        assert adding_task_data == dict_data

    def test_to_json(
        self,
        adding_task_dto: SimpleMathTask,
        adding_task_json: str,
    ) -> None:
        """Test the `to_json()` method."""
        assert adding_task_json == adding_task_dto.to_json()
