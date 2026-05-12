from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from src.constants.messages import MESSAGE_ERROR_APP, MESSAGE_NOT_FOUND_DIALOG_TYPE
from src.utils.dialogs import (
    AuthenticationDialogError,
    BaseDialog,
    BaseDialogError,
    BaseDialogNotification,
    BusinessDialogError,
    ConflictDialogError,
    DeprecatedDialogWarning,
    InternalDialogError,
    NotFoundDialogError,
    SuccessDialogInformation,
    ValidationDialogError,
)


class _WarningTypeDialog(BaseDialog):
    dialog_type = BaseDialog.WARNING
    message = "warning message"


class _InfoTypeDialog(BaseDialog):
    dialog_type = BaseDialog.INFO
    message = "info message"


class _UnknownTypeDialog(BaseDialog):
    dialog_type = "not_a_valid_type"
    message = "unknown message"


class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message_is_error_app(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_overrides_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom error")

        assert dialog.message == "custom error"

    def test_no_message_arg_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.message is not None
        assert dialog.message != ""

    def test_title_is_error_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()

        assert dialog.title == "Error"

    def test_title_is_warning_for_warning_type(self) -> None:
        dialog: _WarningTypeDialog = _WarningTypeDialog()

        assert dialog.title == "Warning"

    def test_title_is_information_for_info_type(self) -> None:
        dialog: _InfoTypeDialog = _InfoTypeDialog()

        assert dialog.title == "Information"

    def test_to_dict_has_required_keys(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")

        result: dict[str, Any] = dialog.to_dict()

        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_returns_correct_values(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")

        result: dict[str, Any] = dialog.to_dict()

        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "test msg"

    def test_open_calls_showerror_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog(message="err msg")
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Error", "err msg")

    def test_open_calls_showwarning_for_warning_type(self) -> None:
        dialog: _WarningTypeDialog = _WarningTypeDialog()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Warning", "warning message")

    def test_open_calls_showinfo_for_info_type(self) -> None:
        dialog: _InfoTypeDialog = _InfoTypeDialog()
        mock_handler: MagicMock = MagicMock()

        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            dialog.open()

        mock_handler.assert_called_once_with("Information", "info message")

    def test_open_falls_back_to_showerror_for_unknown_dialog_type(self) -> None:
        dialog: _UnknownTypeDialog = _UnknownTypeDialog()

        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()

        mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_is_base_dialog(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, BaseDialog)

    def test_is_exception(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert isinstance(error, Exception)

    def test_dialog_type_is_error(self) -> None:
        error: BaseDialogError = BaseDialogError()

        assert error.dialog_type == BaseDialog.ERROR

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()


class TestValidationDialogError:
    def test_inherits_from_base_dialog_error(self) -> None:
        assert issubclass(ValidationDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        error: ValidationDialogError = ValidationDialogError()

        assert error.message == "Validation error"

    def test_custom_message_overrides_default(self) -> None:
        error: ValidationDialogError = ValidationDialogError(message="bad input")

        assert error.message == "bad input"


class TestAuthenticationDialogError:
    def test_inherits_from_base_dialog_error(self) -> None:
        assert issubclass(AuthenticationDialogError, BaseDialogError)

    def test_has_default_message(self) -> None:
        error: AuthenticationDialogError = AuthenticationDialogError()

        assert error.message != ""


class TestNotFoundDialogError:
    def test_inherits_from_base_dialog_error(self) -> None:
        assert issubclass(NotFoundDialogError, BaseDialogError)

    def test_has_default_message(self) -> None:
        error: NotFoundDialogError = NotFoundDialogError()

        assert error.message != ""


class TestConflictDialogError:
    def test_inherits_from_base_dialog_error(self) -> None:
        assert issubclass(ConflictDialogError, BaseDialogError)

    def test_has_default_message(self) -> None:
        error: ConflictDialogError = ConflictDialogError()

        assert error.message != ""


class TestBusinessDialogError:
    def test_inherits_from_base_dialog_error(self) -> None:
        assert issubclass(BusinessDialogError, BaseDialogError)

    def test_has_default_message(self) -> None:
        error: BusinessDialogError = BusinessDialogError()

        assert error.message != ""


class TestInternalDialogError:
    def test_inherits_from_base_dialog_error(self) -> None:
        assert issubclass(InternalDialogError, BaseDialogError)

    def test_has_default_message(self) -> None:
        error: InternalDialogError = InternalDialogError()

        assert error.message != ""


class TestBaseDialogNotification:
    def test_inherits_from_base_dialog(self) -> None:
        assert issubclass(BaseDialogNotification, BaseDialog)

    def test_is_not_an_exception(self) -> None:
        assert not issubclass(BaseDialogNotification, Exception)


class TestDeprecatedDialogWarning:
    def test_dialog_type_is_warning(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert dialog.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        dialog: DeprecatedDialogWarning = DeprecatedDialogWarning()

        assert dialog.message == "This feature is deprecated"


class TestSuccessDialogInformation:
    def test_dialog_type_is_info(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()

        assert dialog.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        dialog: SuccessDialogInformation = SuccessDialogInformation()

        assert dialog.message == "Operation completed successfully"
