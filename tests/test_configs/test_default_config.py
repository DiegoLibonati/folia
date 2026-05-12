import os
from unittest.mock import patch

from src.configs.default_config import DefaultConfig


class TestDefaultConfig:
    def test_debug_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.DEBUG is False

    def test_testing_is_false_by_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert config.TESTING is False

    def test_tz_has_a_non_empty_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert isinstance(config.TZ, str)
        assert config.TZ != ""

    def test_env_name_has_a_non_empty_default(self) -> None:
        config: DefaultConfig = DefaultConfig()

        assert isinstance(config.ENV_NAME, str)
        assert config.ENV_NAME != ""

    def test_tz_is_overridden_by_env_var(self) -> None:
        with patch.dict(os.environ, {"TZ": "UTC"}):
            config: DefaultConfig = DefaultConfig()

        assert config.TZ == "UTC"

    def test_env_name_is_overridden_by_env_var(self) -> None:
        with patch.dict(os.environ, {"ENV_NAME": "custom-app"}):
            config: DefaultConfig = DefaultConfig()

        assert config.ENV_NAME == "custom-app"
