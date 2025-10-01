```python
# Import the logging module for handling program logs
import logging

# Configure the basic logging settings, including the log file name, log level, and log format
logging.basicConfig(
    # Specify the log file where log messages will be written
    filename='programLog.txt', 
    # Set the log level to DEBUG, which will capture all log messages
    level=logging.DEBUG, 
    # Define the log format, including timestamp, log level, and log message
    format=' %(asctime)s -  %(levelname)s -  %(message)s'
)

# Log a debug message indicating the start of the program
logging.debug('Start of program')
```