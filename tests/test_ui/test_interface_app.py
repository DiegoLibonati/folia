import tkinter as tk
from unittest.mock import MagicMock, patch

import pytest

from src.configs.default_config import DefaultConfig
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.fixture(scope="function")
def app(root: tk.Tk) -> InterfaceApp:
    config: DefaultConfig = DefaultConfig()
    styles: Styles = Styles()
    with patch.object(root, "iconbitmap"):
        instance: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)
    return instance


class TestInterfaceApp:
    def test_is_created_successfully(self, app: InterfaceApp) -> None:
        assert app is not None

    def test_save_config_font_raises_when_font_is_empty(self, app: InterfaceApp) -> None:
        with pytest.raises(ValidationDialogError):
            app._save_config_font("", "12")

    def test_save_config_font_raises_when_size_is_empty(self, app: InterfaceApp) -> None:
        with pytest.raises(ValidationDialogError):
            app._save_config_font("Arial", "")

    def test_save_config_font_raises_when_size_is_not_integer(self, app: InterfaceApp) -> None:
        with pytest.raises(ValidationDialogError):
            app._save_config_font("Arial", "abc")

    def test_save_config_font_raises_when_size_is_float_string(self, app: InterfaceApp) -> None:
        with pytest.raises(ValidationDialogError):
            app._save_config_font("Arial", "12.5")

    def test_save_config_font_calls_set_font_with_valid_inputs(self, app: InterfaceApp) -> None:
        app._main_view.set_font = MagicMock()
        app._save_config_font("Arial", "14")
        app._main_view.set_font.assert_called_once_with("Arial", 14)

    def test_save_config_font_converts_size_to_int(self, app: InterfaceApp) -> None:
        app._main_view.set_font = MagicMock()
        app._save_config_font("Roboto", "20")
        args: tuple[str, int] = app._main_view.set_font.call_args[0]
        assert isinstance(args[1], int)
        assert args[1] == 20

    def test_delete_txt_clears_text(self, app: InterfaceApp) -> None:
        app._main_view.set_text("hello")
        app._delete_txt()
        assert app._main_view.get_text().strip() == ""

    def test_save_file_calls_file_service(self, app: InterfaceApp) -> None:
        app._main_view.set_text("content")
        with patch("src.ui.interface_app.FileService.save_file") as mock_save:
            app._save_file()
        mock_save.assert_called_once()

    def test_get_txt_from_file_sets_text_when_content_returned(self, app: InterfaceApp) -> None:
        app._main_view.clear_text()
        with patch("src.ui.interface_app.FileService.open_file", return_value="file content"):
            app._get_txt_from_file()
        assert "file content" in app._main_view.get_text()

    def test_get_txt_from_file_does_nothing_when_none_returned(self, app: InterfaceApp) -> None:
        app._main_view.clear_text()
        with patch("src.ui.interface_app.FileService.open_file", return_value=None):
            app._get_txt_from_file()
        assert app._main_view.get_text().strip() == ""
