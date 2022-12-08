import logging

from .api_settings import ApiSettings
from .app_init import AppInitializer
from .db import assemble_database_url
from .log_utils import configure_logging

log_level = configure_logging()

logger = logging.getLogger(__name__)
logger.info("Initializing api...")

settings = ApiSettings()
app = AppInitializer(settings).create_app()

logger.info("Starting up")
logger.info(assemble_database_url(settings))
