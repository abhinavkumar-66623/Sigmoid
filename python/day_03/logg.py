import logging
import sys
from logging.handlers import RotatingFileHandler


FORMATTER = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

LOG_FILE = "helper.log"

def get_file_handler():
    file_handler = RotatingFileHandler(
        LOG_FILE,
        mode="a",
        maxBytes=10,      # 1 KB for demonstration
        backupCount=5
    )
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler())
    logger.propagate = False
    return logger


log = get_logger("loggy")

# log.debug("This is a debug message")
# log.info("This is an info message")
# log.warning("This is a warning message")
# log.error("This is an error message")
# log.critical("This is a critical message")

def main():
    try:
        result = 10 / 0
        print(result)
    except Exception as e:
        log.error(e)

main()


# try:
#     num1=int(input("Enter the num1: "))
#     num2=int(input("Enter the num2: "))
#     print(num1/num2)
# except ZeroDivisionError :
#     print("cannot divide")
# except ValueError as v:
#     log.error(v)
#     print("please enter valid integer")
# except:
#     print("unexpected error")
# finally:
#     print("cleanup code")
# print("code completed")