from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.error_handler import error_handler


class TestErrorHandler:
    def test_calls_open_when_exc_is_base_dialog(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="bad input")
        exc.open = MagicMock()
        error_handler(type(exc), exc, None)
        exc.open.assert_called_once()

    def test_creates_internal_dialog_when_exc_is_not_base_dialog(self) -> None:
        exc: ValueError = ValueError("something broke")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
        mock_internal.assert_called_once_with(message="something broke")

    def test_calls_open_on_internal_dialog_when_exc_is_not_base_dialog(self) -> None:
        exc: RuntimeError = RuntimeError("runtime fail")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
        mock_instance.open.assert_called_once()

    def test_does_not_create_internal_dialog_when_exc_is_base_dialog(self) -> None:
        exc: ValidationDialogError = ValidationDialogError()
        exc.open = MagicMock()
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            error_handler(type(exc), exc, None)
        mock_internal.assert_not_called()

    def test_passes_exception_message_to_internal_dialog(self) -> None:
        exc: TypeError = TypeError("type mismatch")
        with patch("src.utils.error_handler.InternalDialogError") as mock_internal:
            mock_instance: MagicMock = MagicMock()
            mock_internal.return_value = mock_instance
            error_handler(type(exc), exc, None)
        mock_internal.assert_called_once_with(message="type mismatch")
