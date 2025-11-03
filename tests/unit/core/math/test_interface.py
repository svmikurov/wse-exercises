"""Defines tests for base class for tasks."""

import json
from typing import Any

from wse_exercises.core.math.task import CalcTask


class TestPublicInterface:
    """Test API."""

    def test_from_dict(
        self,
        adding_task_dto: CalcTask,
        adding_task_data: dict[str, Any],
    ) -> None:
        """Test the `from_dict()` method."""
        task = CalcTask.from_dict(adding_task_data)
        assert adding_task_dto == task

    def test_from_json(
        self,
        adding_task_dto: CalcTask,
        adding_task_json: str,
    ) -> None:
        """Test the `from_json()` method."""
        task = CalcTask.from_json(adding_task_json)
        assert adding_task_dto == task

    def test_to_dict(
        self,
        adding_task_dto: CalcTask,
        adding_task_data: dict[str, Any],
    ) -> None:
        """Test the `to_dict()` method."""
        dict_data = adding_task_dto.to_dict()
        assert adding_task_data == dict_data

    def test_to_json(
        self,
        adding_task_dto: CalcTask,
        adding_task_json: str,
    ) -> None:
        """Test the `to_json()` method."""
        expected_data = json.loads(adding_task_json)
        actual_data = json.loads(adding_task_dto.to_json())

        expected_data = self._normalize_datetime_format(expected_data)
        actual_data = self._normalize_datetime_format(actual_data)

        assert expected_data == actual_data

    def _normalize_datetime_format(
        self, data: dict[str, object]
    ) -> dict[str, object]:
        """Normalize datetime format for comparison."""
        if 'created_at' in data and isinstance(data['created_at'], str):
            dt_str = data['created_at']
            if dt_str.endswith('Z'):
                data['created_at'] = dt_str[:-1] + '+00:00'
            elif dt_str.endswith('+00:00'):
                pass
        return data
