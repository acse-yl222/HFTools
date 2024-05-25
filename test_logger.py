import logging
from transformers import logging as hf_logging

# Define a custom format
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Set up Python's built-in logger with the custom format
logging.basicConfig(filename='logfile.log', level=logging.INFO, format=format)

# Set up the Hugging Face logger
hf_logging.set_verbosity_info()

# Get a reference to the logger
logger = logging.Logger(name="test_logger")

# Use the logger
logger.info("This is an informational message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")