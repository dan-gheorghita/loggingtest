# LoggingTest.py

**Program Log Configuration and Debug Message**

This Python code configures basic logging settings and logs a debug message indicating the start of the program.

**Key Features:**

1. **Importing the logging module**: The code imports the `logging` module, which is a built-in Python module for handling program logs.
2. **Configuring basic logging settings**: The `basicConfig` function is used to configure the basic logging settings, including:
	* **Log file**: The log file where log messages will be written is set to `programLog.txt`.
	* **Log level**: The log level is set to `DEBUG`, which will capture all log messages.
	* **Log format**: The log format is defined as `%(asctime)s -  %(levelname)s -  %(message)s`, which includes:
		+ `%(asctime)s`: the timestamp of the log message.
		+ `%(levelname)s`: the log level (e.g., DEBUG, INFO, WARNING,