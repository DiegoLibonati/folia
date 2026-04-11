from src.constants import messages


class TestMessages:
    def test_message_error_app(self) -> None:
        assert messages.MESSAGE_ERROR_APP == "Internal error. Contact a developer."

    def test_message_not_valid_fields(self) -> None:
        assert messages.MESSAGE_NOT_VALID_FIELDS == "You must enter valid fields."

    def test_message_not_valid_field_num(self) -> None:
        assert messages.MESSAGE_NOT_VALID_FIELD_NUM == "You must enter a valid number in the font size."

    def test_message_not_found_dialog_type(self) -> None:
        assert messages.MESSAGE_NOT_FOUND_DIALOG_TYPE == "The type of dialog to display is not found."
