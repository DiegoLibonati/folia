from unittest.mock import MagicMock, patch

from src.utils.dialogs import ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_calls_open_when_exc_is_base_dialog(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="bad input")
        exc.open = MagicMock()
        with patch("src.utils.tkinter_exception_hook.logger"):
            tkinter_exception_hook(type(exc), exc, None)
        exc.open.assert_called_once()

    def test_creates_internal_dialog_when_exc_is_not_base_dialog(self) -> None:
        exc: ValueError = ValueError("something broke")
        with patch("src.utils.tkinter_exception_hook.logger"):
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
                mock_instance: MagicMock = MagicMock()
                mock_internal.return_value = mock_instance
                tkinter_exception_hook(type(exc), exc, None)
        mock_internal.assert_called_once_with(message="something broke")

    def test_calls_open_on_internal_dialog_when_exc_is_not_base_dialog(self) -> None:
        exc: RuntimeError = RuntimeError("runtime fail")
        with patch("src.utils.tkinter_exception_hook.logger"):
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
                mock_instance: MagicMock = MagicMock()
                mock_internal.return_value = mock_instance
                tkinter_exception_hook(type(exc), exc, None)
        mock_instance.open.assert_called_once()

    def test_does_not_create_internal_dialog_when_exc_is_base_dialog(self) -> None:
        exc: ValidationDialogError = ValidationDialogError()
        exc.open = MagicMock()
        with patch("src.utils.tkinter_exception_hook.logger"):
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
                tkinter_exception_hook(type(exc), exc, None)
        mock_internal.assert_not_called()

    def test_passes_exception_message_to_internal_dialog(self) -> None:
        exc: TypeError = TypeError("type mismatch")
        with patch("src.utils.tkinter_exception_hook.logger"):
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
                mock_instance: MagicMock = MagicMock()
                mock_internal.return_value = mock_instance
                tkinter_exception_hook(type(exc), exc, None)
        mock_internal.assert_called_once_with(message="type mismatch")

    def test_logs_error_when_exc_is_base_dialog(self) -> None:
        exc: ValidationDialogError = ValidationDialogError(message="bad input")
        exc.open = MagicMock()
        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            tkinter_exception_hook(type(exc), exc, None)
        mock_logger.error.assert_called_once()

    def test_logs_error_when_exc_is_not_base_dialog(self) -> None:
        exc: RuntimeError = RuntimeError("crash")
        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
                mock_internal.return_value = MagicMock()
                tkinter_exception_hook(type(exc), exc, None)
        mock_logger.error.assert_called_once()

    def test_log_detail_contains_exception_text(self) -> None:
        exc: ValueError = ValueError("important error text")
        with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
            with patch("src.utils.tkinter_exception_hook.InternalDialogError") as mock_internal:
                mock_internal.return_value = MagicMock()
                tkinter_exception_hook(type(exc), exc, None)
        logged_detail: str = mock_logger.error.call_args[0][1]
        assert "important error text" in logged_detail
