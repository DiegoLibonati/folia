import tkinter as tk
from unittest.mock import MagicMock

import pytest

from src.ui.styles import Styles
from src.ui.views.main_view import MainView


@pytest.fixture
def styles() -> Styles:
    return Styles()


@pytest.fixture
def main_view(root: tk.Tk, styles: Styles) -> MainView:
    view: MainView = MainView(
        root=root,
        styles=styles,
        on_open=MagicMock(),
        on_save=MagicMock(),
        on_delete=MagicMock(),
        on_change_font=MagicMock(),
    )
    yield view
    view.destroy()


class TestMainView:
    def test_is_a_frame(self, main_view: MainView) -> None:
        assert isinstance(main_view, tk.Frame)

    def test_get_text_returns_trailing_newline_when_empty(self, main_view: MainView) -> None:
        result: str = main_view.get_text()

        assert result == "\n"

    def test_set_text_inserts_content(self, main_view: MainView) -> None:
        main_view.set_text("hello world")

        result: str = main_view.get_text()

        assert "hello world" in result

    def test_set_text_replaces_existing_content(self, main_view: MainView) -> None:
        main_view.set_text("old content")

        main_view.set_text("new content")

        result: str = main_view.get_text()
        assert "new content" in result
        assert "old content" not in result

    def test_clear_text_empties_the_widget(self, main_view: MainView) -> None:
        main_view.set_text("some content to clear")

        main_view.clear_text()

        assert main_view.get_text().strip() == ""

    def test_set_font_changes_the_text_widget_font(self, main_view: MainView) -> None:
        initial_font: str = str(main_view._text_entry.cget("font"))

        main_view.set_font("Courier", 20)

        updated_font: str = str(main_view._text_entry.cget("font"))
        assert updated_font != initial_font
