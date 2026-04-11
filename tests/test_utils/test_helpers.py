import os
import sys
from unittest.mock import patch

from src.utils.helpers import resource_path


class TestResourcePath:
    def test_returns_string(self) -> None:
        result: str = resource_path("some/path")
        assert isinstance(result, str)

    def test_joins_with_cwd_when_no_meipass(self) -> None:
        result: str = resource_path("assets/icon.ico")
        expected: str = os.path.join(os.path.abspath("."), "assets/icon.ico")
        assert result == expected

    def test_joins_with_meipass_when_available(self) -> None:
        fake_meipass: str = "/fake/meipass"
        with patch.object(sys, "_MEIPASS", fake_meipass, create=True):
            result: str = resource_path("assets/icon.ico")
        expected: str = os.path.join(fake_meipass, "assets/icon.ico")
        assert result == expected

    def test_relative_path_is_included_in_result(self) -> None:
        result: str = resource_path("foo/bar.txt")
        assert "foo" in result
        assert "bar.txt" in result

    def test_empty_relative_path(self) -> None:
        result: str = resource_path("")
        assert os.path.normpath(result) == os.path.normpath(os.path.abspath("."))

    def test_nested_path_is_preserved(self) -> None:
        result: str = resource_path("a/b/c/d.ico")
        assert "a" in result
        assert "d.ico" in result
