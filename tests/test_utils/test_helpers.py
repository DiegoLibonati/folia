import os
import sys
from unittest.mock import patch

from src.utils.helpers import resource_path


class TestResourcePath:
    def test_returns_string(self) -> None:
        result: str = resource_path("some/path")

        assert isinstance(result, str)

    def test_result_contains_relative_portion(self) -> None:
        result: str = resource_path("assets/icon.ico")

        assert "assets" in result
        assert "icon.ico" in result

    def test_uses_meipass_base_when_available(self) -> None:
        with patch.object(sys, "_MEIPASS", "/frozen/base", create=True):
            result: str = resource_path("assets/icon.ico")

        assert result.startswith("/frozen/base")

    def test_uses_cwd_base_without_meipass(self) -> None:
        expected_base: str = os.path.abspath(".")

        result: str = resource_path("some/path")

        assert result.startswith(expected_base)
