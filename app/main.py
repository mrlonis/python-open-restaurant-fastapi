import logging

from .app_init import AppInitializer
from .config import DatabaseSettings
from .database import assemble_database_url
from .utils import configure_logging

configure_logging()

logger = logging.getLogger(__name__)
logger.info("Initializing api...")

app = AppInitializer().create_app()

logger.info("Starting up")
logger.info(assemble_database_url(DatabaseSettings()))
