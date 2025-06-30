"""Defines tests for base class for tasks."""

from typing import Any

from wse_exercises.core.mathem.task import SimpleMathTask


class TestPublicInterface:
    """Test API."""

    def test_from_dict(
        self,
        simple_math_task: SimpleMathTask,
        simple_math_task_dict: dict[str, Any],
    ) -> None:
        """Test the `from_dict()` method."""
        task = SimpleMathTask.from_dict(simple_math_task_dict)
        assert simple_math_task == task

    def test_from_json(
        self,
        simple_math_task: SimpleMathTask,
        simple_math_task_json: str,
    ) -> None:
        """Test the `from_json()` method."""
        task = SimpleMathTask.from_json(simple_math_task_json)
        assert simple_math_task == task

    def test_to_dict(
        self,
        simple_math_task: SimpleMathTask,
        simple_math_task_dict: dict[str, Any],
    ) -> None:
        """Test the `to_dict()` method."""
        dict_data = simple_math_task.to_dict()
        assert simple_math_task_dict == dict_data

    def test_to_json(
        self,
        simple_math_task: SimpleMathTask,
        simple_math_task_json: str,
    ) -> None:
        """Test the `to_json()` method."""
        assert simple_math_task_json == simple_math_task.to_json()
