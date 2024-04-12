**Custom Logger: Enhanced Logging for Your Python Applications**

**Introduction**

This Python package provides a robust and customizable logger that simplifies the process of recording messages and events in your applications. It leverages the power of the `colorlog` library to enhance readability and debugging capabilities.

**Key Features**

* **Flexible Log Levels:** Supports standard logging levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`) to categorize messages based on severity.
* **Colorized Output:** Leverages `colorlog` to display log messages in distinct colors, improving visual clarity.
* **File and Console Logging:** Logs messages to a specified file and optionally to the console for immediate feedback.
* **Customizable Formatting:** Control the appearance of log messages using formatters for both file and console output.
* **Dynamic Console Logging:** Enable or disable console logging at runtime to manage verbosity during development.
* **Handler Management:** Add, remove, or adjust logging handlers to tailor logging behavior.
* **Default Loggers:** Provides convenient wrappers for standard logging methods (`debug`, `info`, `warning`, `error`, `critical`, and `exception`).
* **Session Logging:** Decorator function `log_session` to enclose a block of code with logging messages for session tracking.
* **Log File Reading:** Utility function `read_log_file` to conveniently read and display the contents of the log file.
* **Log File Clearing:** Optional `clear_log_file` method to clear existing log data.

**Installation**

To install the `custom_logger` package from PyPI (the Python Package Index), use the following command in your terminal:

```bash
pip install custom_logger
```

**Usage**

1. **Import the Logger Class:**

   ```python
   from custom_logger import Logger
   ```

2. **Create a Logger Instance:**

   ```python
   logger = Logger(log_name='my_logger', log_file='app.log', log_to_console=True)
   ```

   - `log_name`: A descriptive name for your logger (e.g., 'my_logger').
   - `log_file`: The path to the log file where messages will be saved.
   - `log_to_console` (optional, defaults to `True`): Whether to log messages to the console.

3. **Log Messages:**

   ```python
   logger.log_message('info', 'This is an informative message.')
   logger.warning('This is a warning message.')
   logger.error('This is an error message.')
   logger.critical('This is a critical message.')
   ```

4. **Default Loggers:**

   ```python
   logger.info('This is a general message.')
   logger.warning('This requires attention.')
   logger.exception('An exception occurred!', exc_info=True)  # Optional exception info
   ```

5. **Session Logging:**

   ```python
   @logger.log_session
   def my_function():
       # Your code here
       logger.info('Processing completed.')
   ```

   The `log_session` decorator automatically logs the start and end of the function execution.

6. **Read Log File:**

   ```python
   logger.read_log_file()
   ```

7. **Clear Log File (optional):**

   ```python
   logger.clear_log_file()  # Use with caution
   ```

**Advanced Usage**

* **Dynamic Console Logging:**

  ```python
  logger.disable_console_logging()  # Disable console logging
  logger.enable_console_logging()   # Re-enable console logging
  ```

* **Handler Management:**

   Refer to the source code for details on adding, removing, or modifying logging handlers.

**Customization**

For advanced customization, consult the source code to modify formatting options for file and console output or create custom handlers.

**Contributing**

We welcome contributions to improve this logger. Feel free to submit pull requests on GitHub!

**License**

This project is licensed under the MIT License. See the LICENSE file for details.
