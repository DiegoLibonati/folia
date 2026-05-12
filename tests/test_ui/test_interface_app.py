import tkinter as tk
from unittest.mock import patch

import pytest

from src.configs.default_config import DefaultConfig
from src.constants.messages import MESSAGE_NOT_VALID_FIELD_NUM, MESSAGE_NOT_VALID_FIELDS
from src.ui.interface_app import InterfaceApp
from src.ui.styles import Styles
from src.utils.dialogs import ValidationDialogError


@pytest.fixture
def config() -> DefaultConfig:
    return DefaultConfig()


@pytest.fixture
def styles() -> Styles:
    return Styles()


@pytest.fixture
def app(root: tk.Tk, config: DefaultConfig, styles: Styles) -> InterfaceApp:
    with patch.object(root, "iconbitmap"):
        instance: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)
    yield instance
    instance._main_view.destroy()


class TestInterfaceApp:
    def test_stores_provided_config(
        self, root: tk.Tk, config: DefaultConfig, styles: Styles
    ) -> None:
        with patch.object(root, "iconbitmap"):
            app: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)

        assert app._config is config
        app._main_view.destroy()

    def test_stores_provided_styles(
        self, root: tk.Tk, config: DefaultConfig, styles: Styles
    ) -> None:
        with patch.object(root, "iconbitmap"):
            app: InterfaceApp = InterfaceApp(root=root, config=config, styles=styles)

        assert app._styles is styles
        app._main_view.destroy()

    def test_creates_default_styles_when_none_provided(
        self, root: tk.Tk, config: DefaultConfig
    ) -> None:
        with patch.object(root, "iconbitmap"):
            app: InterfaceApp = InterfaceApp(root=root, config=config)

        assert isinstance(app._styles, Styles)
        app._main_view.destroy()

    def test_save_config_font_raises_when_font_is_empty(self, app: InterfaceApp) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            app._save_config_font("", "12")

        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_save_config_font_raises_when_size_is_empty(self, app: InterfaceApp) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            app._save_config_font("Arial", "")

        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELDS

    def test_save_config_font_raises_when_size_is_not_numeric(self, app: InterfaceApp) -> None:
        with pytest.raises(ValidationDialogError) as exc_info:
            app._save_config_font("Arial", "abc")

        assert exc_info.value.message == MESSAGE_NOT_VALID_FIELD_NUM

    def test_save_config_font_calls_set_font_with_int_size(self, app: InterfaceApp) -> None:
        with patch.object(app._main_view, "set_font") as mock_set_font:
            app._save_config_font("Arial", "14")

        mock_set_font.assert_called_once_with("Arial", 14)

    def test_get_txt_from_file_sets_text_when_content_is_returned(self, app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.FileService.open_file", return_value="file content"):
            with patch.object(app._main_view, "set_text") as mock_set_text:
                app._get_txt_from_file()

        mock_set_text.assert_called_once_with("file content")

    def test_get_txt_from_file_does_not_set_text_when_no_file_is_selected(
        self, app: InterfaceApp
    ) -> None:
        with patch("src.ui.interface_app.FileService.open_file", return_value=None):
            with patch.object(app._main_view, "set_text") as mock_set_text:
                app._get_txt_from_file()

        mock_set_text.assert_not_called()

    def test_save_file_passes_text_content_to_file_service(self, app: InterfaceApp) -> None:
        with patch.object(app._main_view, "get_text", return_value="editor content"):
            with patch("src.ui.interface_app.FileService.save_file") as mock_save:
                app._save_file()

        mock_save.assert_called_once_with("editor content")

    def test_delete_txt_clears_the_main_view(self, app: InterfaceApp) -> None:
        with patch.object(app._main_view, "clear_text") as mock_clear:
            app._delete_txt()

        mock_clear.assert_called_once()

    def test_open_win_config_font_creates_font_config_view(self, app: InterfaceApp) -> None:
        with patch("src.ui.interface_app.FontConfigView") as mock_view_cls:
            app._open_win_config_font()

        mock_view_cls.assert_called_once()
