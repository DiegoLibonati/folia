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


class TestBaseDialog:
    def test_default_dialog_type_is_error(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.dialog_type == BaseDialog.ERROR

    def test_default_message(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.message == MESSAGE_ERROR_APP

    def test_custom_message_is_set(self) -> None:
        dialog: BaseDialog = BaseDialog(message="custom msg")
        assert dialog.message == "custom msg"

    def test_message_none_keeps_class_default(self) -> None:
        dialog: BaseDialog = BaseDialog(message=None)
        assert dialog.message == MESSAGE_ERROR_APP

    def test_title_for_error_type(self) -> None:
        dialog: BaseDialog = BaseDialog()
        assert dialog.title == "Error"

    def test_title_for_warning_type(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING

        dialog: WarningDialog = WarningDialog()
        assert dialog.title == "Warning"

    def test_title_for_info_type(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO

        dialog: InfoDialog = InfoDialog()
        assert dialog.title == "Information"

    def test_title_defaults_to_error_for_unknown_type(self) -> None:
        class UnknownDialog(BaseDialog):
            dialog_type = "UNKNOWN"

        dialog: UnknownDialog = UnknownDialog()
        assert dialog.title == "Error"

    def test_to_dict_contains_required_keys(self) -> None:
        dialog: BaseDialog = BaseDialog()
        result: dict[str, Any] = dialog.to_dict()
        assert "dialog_type" in result
        assert "title" in result
        assert "message" in result

    def test_to_dict_values_match_instance(self) -> None:
        dialog: BaseDialog = BaseDialog(message="test msg")
        result: dict[str, Any] = dialog.to_dict()
        assert result["dialog_type"] == BaseDialog.ERROR
        assert result["title"] == "Error"
        assert result["message"] == "test msg"

    def test_open_error_calls_showerror(self) -> None:
        dialog: BaseDialog = BaseDialog()
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.ERROR: mock_handler}):
            dialog.open()
        mock_handler.assert_called_once_with("Error", MESSAGE_ERROR_APP)

    def test_open_warning_calls_showwarning(self) -> None:
        class WarningDialog(BaseDialog):
            dialog_type = BaseDialog.WARNING
            message = "warn"

        dialog: WarningDialog = WarningDialog()
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.WARNING: mock_handler}):
            dialog.open()
        mock_handler.assert_called_once_with("Warning", "warn")

    def test_open_info_calls_showinfo(self) -> None:
        class InfoDialog(BaseDialog):
            dialog_type = BaseDialog.INFO
            message = "info msg"

        dialog: InfoDialog = InfoDialog()
        mock_handler: MagicMock = MagicMock()
        with patch.dict(BaseDialog._HANDLERS, {BaseDialog.INFO: mock_handler}):
            dialog.open()
        mock_handler.assert_called_once_with("Information", "info msg")

    def test_open_unknown_type_calls_showerror_with_not_found_message(self) -> None:
        class UnknownDialog(BaseDialog):
            dialog_type = "UNKNOWN"
            message = "x"

        dialog: UnknownDialog = UnknownDialog()
        with patch("src.utils.dialogs.messagebox.showerror") as mock_showerror:
            dialog.open()
        mock_showerror.assert_called_once_with(BaseDialog.ERROR, MESSAGE_NOT_FOUND_DIALOG_TYPE)


class TestBaseDialogError:
    def test_is_exception(self) -> None:
        assert issubclass(BaseDialogError, Exception)

    def test_is_base_dialog(self) -> None:
        assert issubclass(BaseDialogError, BaseDialog)

    def test_dialog_type_is_error(self) -> None:
        assert BaseDialogError.dialog_type == BaseDialog.ERROR

    def test_can_be_raised_and_caught(self) -> None:
        with pytest.raises(BaseDialogError):
            raise BaseDialogError()

    def test_custom_message_on_raise(self) -> None:
        with pytest.raises(BaseDialogError) as exc_info:
            raise BaseDialogError(message="fail")
        assert exc_info.value.message == "fail"

    def test_is_catchable_as_exception(self) -> None:
        with pytest.raises(Exception):
            raise BaseDialogError()


class TestValidationDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert issubclass(ValidationDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        assert ValidationDialogError.message == "Validation error"

    def test_custom_message_overrides_default(self) -> None:
        err: ValidationDialogError = ValidationDialogError(message="invalid input")
        assert err.message == "invalid input"

    def test_can_be_raised(self) -> None:
        with pytest.raises(ValidationDialogError):
            raise ValidationDialogError()


class TestAuthenticationDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert issubclass(AuthenticationDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        assert AuthenticationDialogError.message == "Authentication error"


class TestNotFoundDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert issubclass(NotFoundDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        assert NotFoundDialogError.message == "Resource not found"


class TestConflictDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert issubclass(ConflictDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        assert ConflictDialogError.message == "Conflict error"


class TestBusinessDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert issubclass(BusinessDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        assert BusinessDialogError.message == "Business rule violated"


class TestInternalDialogError:
    def test_is_base_dialog_error(self) -> None:
        assert issubclass(InternalDialogError, BaseDialogError)

    def test_default_message(self) -> None:
        assert InternalDialogError.message == "Internal error"


class TestBaseDialogNotification:
    def test_is_base_dialog(self) -> None:
        assert issubclass(BaseDialogNotification, BaseDialog)

    def test_is_not_exception(self) -> None:
        assert not issubclass(BaseDialogNotification, Exception)


class TestDeprecatedDialogWarning:
    def test_is_base_dialog_notification(self) -> None:
        assert issubclass(DeprecatedDialogWarning, BaseDialogNotification)

    def test_dialog_type_is_warning(self) -> None:
        assert DeprecatedDialogWarning.dialog_type == BaseDialog.WARNING

    def test_default_message(self) -> None:
        assert DeprecatedDialogWarning.message == "This feature is deprecated"


class TestSuccessDialogInformation:
    def test_is_base_dialog_notification(self) -> None:
        assert issubclass(SuccessDialogInformation, BaseDialogNotification)

    def test_dialog_type_is_info(self) -> None:
        assert SuccessDialogInformation.dialog_type == BaseDialog.INFO

    def test_default_message(self) -> None:
        assert SuccessDialogInformation.message == "Operation completed successfully"
