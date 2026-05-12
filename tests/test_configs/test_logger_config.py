import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger_instance(self) -> None:
        logger: logging.Logger = setup_logger()

        assert isinstance(logger, logging.Logger)

    def test_default_name_is_tkinter_app(self) -> None:
        logger: logging.Logger = setup_logger()

        assert logger.name == "tkinter-app"

    def test_custom_name_is_used(self) -> None:
        logger: logging.Logger = setup_logger("my-custom-logger")

        assert logger.name == "my-custom-logger"

    def test_logger_has_at_least_one_handler(self) -> None:
        logger: logging.Logger = setup_logger("handler-test-logger")

        assert len(logger.handlers) >= 1

    def test_calling_twice_does_not_add_duplicate_handlers(self) -> None:
        logger: logging.Logger = setup_logger("idempotent-logger")
        count_after_first: int = len(logger.handlers)

        setup_logger("idempotent-logger")

        assert len(logger.handlers) == count_after_first

    def test_logger_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("level-check-logger")

        assert logger.level == logging.DEBUG
