import logging

#  this Configures the logging system
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#  this Creates a logger for this module
logger = logging.getLogger(__name__)

# Example usage of the logger
if __name__ == "__main__":
    logger.debug("Debugging information: This is a debug message.")
    logger.info("Informational message: The application has started.")
    logger.warning("Warning: This is a warning message.")
    logger.error("Error: An error has occurred.")
    logger.critical("Critical: A critical issue has been encountered.")