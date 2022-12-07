import logging

from .app_init import AppInitializer
from .config import ApiSettings
from .utils import configure_logging

log_level = configure_logging()

logger = logging.getLogger(__name__)
logger.info("Initializing api...")

settings = ApiSettings()
app = AppInitializer(settings).create_app()

logger.info("Starting up")
logger.info(settings.database_url)
