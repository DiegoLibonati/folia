import tkinter as tk
from unittest.mock import MagicMock, patch

import pytest

from src.ui.styles import Styles
from src.ui.views.font_config_view import FontConfigView


@pytest.fixture
def styles() -> Styles:
    return Styles()


@pytest.fixture
def on_save() -> MagicMock:
    return MagicMock()


@pytest.fixture
def font_config_view(root: tk.Tk, styles: Styles, on_save: MagicMock) -> FontConfigView:
    with patch.object(tk.Toplevel, "iconbitmap"):
        view: FontConfigView = FontConfigView(root=root, styles=styles, on_save=on_save)
    yield view
    try:
        view.destroy()
    except Exception:
        pass


class TestFontConfigView:
    def test_is_a_toplevel(self, font_config_view: FontConfigView) -> None:
        assert isinstance(font_config_view, tk.Toplevel)

    def test_has_font_config_form(self, font_config_view: FontConfigView) -> None:
        assert font_config_view._font_config_form is not None

    def test_has_entry_number_as_string_var(self, font_config_view: FontConfigView) -> None:
        assert isinstance(font_config_view._entry_number, tk.StringVar)

    def test_handle_save_calls_on_save_with_font_and_size(
        self, font_config_view: FontConfigView, on_save: MagicMock
    ) -> None:
        font_config_view._font_config_form._combo_fonts.set("Arial")
        font_config_view._entry_number.set("12")

        font_config_view._handle_save()

        on_save.assert_called_once_with("Arial", "12")
