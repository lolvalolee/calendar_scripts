import os
import sys

from logging import getLogger, StreamHandler

logger = getLogger(__name__)
logger.setLevel(os.environ.get("LOGGING_LEVEL", "INFO"))
logger.addHandler(StreamHandler(sys.stdout))
