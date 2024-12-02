# **ultra-logger**

**ultra-logger** is a customizable, visually enhanced Python logging library designed to simplify logging for developers. It integrates `colorlog` for colorful, readable logs and provides features such as console/file logging, log session tracking, and log file management.

---

## **Features**

- **Color-coded Console Logs**: Easy to read with distinct colors for each log level.
- **File Logging**: Saves logs to a file for later analysis.
- **Console Logging Control**: Toggle console logging on or off dynamically.
- **Session Tracking**: Log the start and end of a specific session or function.
- **Custom Log Levels**: Supports all standard log levels (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
- **Log File Management**: Read and clear log files effortlessly.

---

## **Installation**

Install `ultra-logger` directly from PyPI:

```bash
pip install ultra-logger
```

---

## **Usage**

Here's how to use **ultra-logger** in your Python projects:

### **Basic Setup**

```python
from ultra_logger import Logger

# Create a Logger instance
logger = Logger(
    log_name="my_app",
    log_file="app.log",
    log_to_console=True,   # Enable console logging
    clear_previous=False,  # Don't clear the log file at initialization
)

# Log messages
logger.info("This is an informational message.")
logger.warning("This is a warning.")
logger.error("This is an error message.")
logger.critical("Critical issue encountered!")
```

### **Advanced Features**

#### **Log Sessions**

Easily track the start and end of a session using the `@log_session` decorator:

```python
@logger.log_session
def perform_task():
    logger.info("Task in progress...")
    # Your logic here
    logger.info("Task completed!")

perform_task()
```

#### **Enable/Disable Console Logging**

Control logging dynamically:

```python
logger.disable_console_logging()  # Suppress console logs
logger.info("This won't appear in the console.")

logger.enable_console_logging()  # Re-enable console logging
logger.info("This will appear in the console.")
```

#### **Read or Clear Log Files**

```python
# Read all log entries from the log file
logger.read_log_file()

# Clear the log file
logger.clear_log_file()
logger.info("The log file is now cleared.")
```

#### **Custom Log Levels**

Use default logging methods for convenience:

```python
logger.debug("Debugging details.")
logger.error("Error encountered!")
logger.exception("Exception occurred with traceback.", exc_info=True)
```

---

## **Log Format**

**Console Logs**: Color-coded for easy readability:

```
2024-11-25 12:34:56 - INFO    - Informational message
2024-11-25 12:34:57 - WARNING - Warning message
2024-11-25 12:34:58 - ERROR   - Error message
2024-11-25 12:34:59 - CRITICAL- Critical issue
```

**File Logs**: Saved in plain text for detailed analysis:

```
2024-11-25 12:34:56 - INFO    - Informational message
2024-11-25 12:34:57 - WARNING - Warning message
```

---

## **Testing**

Run the following tests using `pytest` to ensure the logger works as expected:

```bash
pytest tests/
```

---

## **Contributing**

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`feature/my-feature`).
3. Commit your changes.
4. Push the branch and submit a pull request.

---

## **License**

This project is licensed under the MIT License.

---

## **Author**

Developed by **Om Singh Chandel**. Feel free to reach out for suggestions or issues at [omchandel1703@gmail.com](mailto:omchandel1703@gmail.com).
