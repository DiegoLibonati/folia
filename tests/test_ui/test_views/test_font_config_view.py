import tkinter as tk
from unittest.mock import MagicMock, patch

import pytest

from src.ui.styles import Styles
from src.ui.views.font_config_view import FontConfigView


@pytest.fixture(scope="function")
def view(root: tk.Tk) -> FontConfigView:
    styles: Styles = Styles()
    with patch("tkinter.Toplevel.iconbitmap"):
        instance: FontConfigView = FontConfigView(root=root, styles=styles, on_save=MagicMock())
    return instance


class TestFontConfigView:
    def test_is_created_successfully(self, view: FontConfigView) -> None:
        assert view is not None

    def test_is_toplevel(self, view: FontConfigView) -> None:
        assert isinstance(view, tk.Toplevel)

    def test_entry_number_initial_value_is_empty(self, view: FontConfigView) -> None:
        assert view._entry_number.get() == ""

    def test_entry_number_set(self, view: FontConfigView) -> None:
        view._entry_number.set("12")
        assert view._entry_number.get() == "12"

    def test_entry_number_set_multiple_values(self, view: FontConfigView) -> None:
        view._entry_number.set("8")
        assert view._entry_number.get() == "8"
        view._entry_number.set("24")
        assert view._entry_number.get() == "24"

    def test_handle_save_calls_on_save_with_font_and_size(self, root: tk.Tk) -> None:
        mock_on_save: MagicMock = MagicMock()
        with patch("tkinter.Toplevel.iconbitmap"):
            instance: FontConfigView = FontConfigView(root=root, styles=Styles(), on_save=mock_on_save)
        instance._font_config_form.get_font = MagicMock(return_value="Arial")
        instance._entry_number.set("12")
        with patch.object(instance, "destroy"):
            instance._handle_save()
        mock_on_save.assert_called_once_with("Arial", "12")

    def test_handle_save_destroys_window(self, root: tk.Tk) -> None:
        mock_on_save: MagicMock = MagicMock()
        with patch("tkinter.Toplevel.iconbitmap"):
            instance: FontConfigView = FontConfigView(root=root, styles=Styles(), on_save=mock_on_save)
        instance._font_config_form.get_font = MagicMock(return_value="Roboto")
        instance._entry_number.set("16")
        with patch.object(instance, "destroy") as mock_destroy:
            instance._handle_save()
        mock_destroy.assert_called_once()

    def test_handle_save_passes_empty_values_when_not_filled(self, root: tk.Tk) -> None:
        mock_on_save: MagicMock = MagicMock()
        with patch("tkinter.Toplevel.iconbitmap"):
            instance: FontConfigView = FontConfigView(root=root, styles=Styles(), on_save=mock_on_save)
        instance._font_config_form.get_font = MagicMock(return_value="")
        with patch.object(instance, "destroy"):
            instance._handle_save()
        mock_on_save.assert_called_once_with("", "")
