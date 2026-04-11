import logging

from src.configs.logger_config import setup_logger


class TestSetupLogger:
    def test_returns_logger(self) -> None:
        logger: logging.Logger = setup_logger()
        assert isinstance(logger, logging.Logger)

    def test_default_name(self) -> None:
        logger: logging.Logger = setup_logger()
        assert logger.name == "tkinter-app"

    def test_custom_name(self) -> None:
        logger: logging.Logger = setup_logger("my-logger")
        assert logger.name == "my-logger"

    def test_level_is_debug(self) -> None:
        logger: logging.Logger = setup_logger("test-level-logger")
        assert logger.level == logging.DEBUG

    def test_has_handlers(self) -> None:
        logger: logging.Logger = setup_logger("test-handlers-logger")
        assert len(logger.handlers) > 0

    def test_no_duplicate_handlers_on_repeated_calls(self) -> None:
        logger_name: str = "test-no-dup-logger"
        setup_logger(logger_name)
        setup_logger(logger_name)
        logger: logging.Logger = setup_logger(logger_name)
        assert len(logger.handlers) == 1
