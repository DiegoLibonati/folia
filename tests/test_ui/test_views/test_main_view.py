import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


@pytest.fixture(scope="function")
def view(root: tk.Tk) -> MainView:
    styles: Styles = Styles()
    return MainView(
        root=root,
        styles=styles,
        on_open=MagicMock(),
        on_save=MagicMock(),
        on_delete=MagicMock(),
        on_change_font=MagicMock(),
    )


class TestMainView:
    def test_is_created_successfully(self, view: MainView) -> None:
        assert view is not None

    def test_is_frame(self, view: MainView) -> None:
        assert isinstance(view, tk.Frame)

    def test_get_text_returns_empty_by_default(self, view: MainView) -> None:
        view.clear_text()
        result: str = view.get_text()
        assert result.strip() == ""

    def test_set_text_inserts_content(self, view: MainView) -> None:
        view.set_text("hello world")
        assert "hello world" in view.get_text()

    def test_clear_text_removes_content(self, view: MainView) -> None:
        view.set_text("some text")
        view.clear_text()
        assert view.get_text().strip() == ""

    def test_set_text_replaces_existing_content(self, view: MainView) -> None:
        view.set_text("first")
        view.set_text("second")
        result: str = view.get_text()
        assert "first" not in result
        assert "second" in result

    def test_set_text_with_multiline_content(self, view: MainView) -> None:
        multiline: str = "line1\nline2\nline3"
        view.set_text(multiline)
        assert "line1" in view.get_text()
        assert "line2" in view.get_text()
        assert "line3" in view.get_text()

    def test_set_font_does_not_raise(self, view: MainView) -> None:
        view.set_font("Arial", 16)

    def test_set_font_updates_text_widget_font(self, view: MainView) -> None:
        view.set_font("Arial", 16)
        font_value: str | tuple[str, str] = view._text_entry["font"]
        assert "Arial" in str(font_value)
        assert "16" in str(font_value)

    def test_get_text_after_set_returns_same_content(self, view: MainView) -> None:
        view.set_text("exact content")
        result: str = view.get_text()
        assert "exact content" in result
