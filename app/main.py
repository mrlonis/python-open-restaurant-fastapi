import logging

from app.app_init import AppInitializer
from app.config.database_settings import DatabaseSettings
from app.database.db import assemble_database_url
from app.utils.log_utils import configure_logging

configure_logging()

logger = logging.getLogger(__name__)
logger.info("Initializing api...")

app = AppInitializer().create_app()

logger.info("Starting up")
logger.info(assemble_database_url(DatabaseSettings()))
