from unittest.mock import MagicMock, patch

from src.utils.dialogs import BaseDialog, InternalDialogError, ValidationDialogError
from src.utils.tkinter_exception_hook import tkinter_exception_hook


class TestTkinterExceptionHook:
    def test_calls_open_on_base_dialog_exceptions(self) -> None:
        dialog: ValidationDialogError = ValidationDialogError(message="test error")

        with patch.object(dialog, "open") as mock_open:
            tkinter_exception_hook(type(dialog), dialog, None)

        mock_open.assert_called_once()

    def test_opens_internal_dialog_for_non_dialog_exceptions(self) -> None:
        exc: ValueError = ValueError("something broke")

        with patch.object(InternalDialogError, "open") as mock_open:
            tkinter_exception_hook(ValueError, exc, None)

        mock_open.assert_called_once()

    # def test_logs_error_for_every_unhandled_exception(self) -> None:
    #     exc: RuntimeError = RuntimeError("runtime error")

    #     with patch("src.utils.tkinter_exception_hook.logger") as mock_logger:
    #         with patch.object(InternalDialogError, "open"):
    #             tkinter_exception_hook(RuntimeError, exc, None)

    #     mock_logger.error.assert_called_once()

    def test_internal_dialog_receives_exception_message(self) -> None:
        exc: ValueError = ValueError("the real message")
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            tkinter_exception_hook(ValueError, exc, None)

        call_args: tuple[str, str] = mock_handler.call_args[0]
        assert "the real message" in call_args[1]
