import pytest

from src.constants.messages import (
    MESSAGE_ERROR_APP,
    MESSAGE_NOT_FOUND_DIALOG_TYPE,
    MESSAGE_NOT_VALID_FIELD_NUM,
    MESSAGE_NOT_VALID_FIELDS,
)


class TestMessages:
    def test_message_error_app_value(self) -> None:
        assert MESSAGE_ERROR_APP == "Internal error. Contact a developer."

    def test_message_not_valid_fields_value(self) -> None:
        assert MESSAGE_NOT_VALID_FIELDS == "You must enter valid fields."

    def test_message_not_valid_field_num_value(self) -> None:
        assert MESSAGE_NOT_VALID_FIELD_NUM == "You must enter a valid number in the font size."

    def test_message_not_found_dialog_type_value(self) -> None:
        assert MESSAGE_NOT_FOUND_DIALOG_TYPE == "The type of dialog to display is not found."

    @pytest.mark.parametrize(
        "message",
        [
            MESSAGE_ERROR_APP,
            MESSAGE_NOT_VALID_FIELDS,
            MESSAGE_NOT_VALID_FIELD_NUM,
            MESSAGE_NOT_FOUND_DIALOG_TYPE,
        ],
    )
    def test_message_is_non_empty_string(self, message: str) -> None:
        assert isinstance(message, str)
        assert message != ""
