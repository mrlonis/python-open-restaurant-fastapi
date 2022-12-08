import logging

from ..config.api_settings import ApiSettings


def configure_logging():
    log_level = ApiSettings().log_level

    if len(logging.getLogger().handlers) > 0:
        # The Lambda environment pre-configures a handler logging to stderr. If a handler is already
        # configured, `.basicConfig` does not execute. Thus we set the level directly.
        if log_level:
            logging.getLogger().setLevel(log_level)
    else:
        logging.basicConfig(level=log_level)
    return log_level
