"""This is a logging library"""
import time

LOG_FILE = "run.log"
MODE = "disabled"

class Logger:
    """Logger, outputs nothing when called. Parent class to other loggers"""
    def message(self, level, msg):
        """Formulates message"""
        return f"[{time.time()}] [{level}] {msg}"
    def error(self, msg):
        """error"""
        self.output(self.message("ERROR", msg))
    def warn(self, msg):
        """warn"""
        self.output(self.message("WARN", msg))
    def info(self, msg):
        """info"""
        self.output(self.message("INFO", msg))
    def output(self, msg):
        """pass"""

class DummyLogger:
    """This logger does absolutely nothing"""
    def error(self, msg):
        """Pass"""
    def warn(self, msg):
        """Pass"""
    def info(self, msg):
        """Pass"""

class TerminalLogger(Logger):
    """Logger that outputs to Terminal"""
    def output(self, msg):
        """Output"""
        print(msg)

class FileLogger(Logger):
    """Logger that outputs to file"""
    def output(self, msg):
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(msg)

class FileTerminalLogger(Logger):
    """logger that outputs to both File and Terminal"""
    def output(self, msg):
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(msg)
        print(msg)

log_class = DummyLogger()

def mode_update(new_mode):
    """Updates the logger module mode"""
    global log_class
    if new_mode == "disabled":
        log_class = DummyLogger

    elif new_mode == "terminal":
        log_class = TerminalLogger

    elif new_mode == "file":
        log_class = FileLogger

    elif new_mode == "file_terminal":
        log_class = FileTerminalLogger

    else:
        raise ValueError(f"Valid Modes are 'disabled', 'terminal' 'file' and\
                'file_terminal'. Mode recived was {new_mode}")

def error(msg):
    """Allows program to call error through module"""
    log_class.error(msg)
def warn(msg):
    """Allows program to call warn through module"""
    log_class.error(msg)
def info(msg):
    """Allows program to call info through module"""
    log_class.info(msg)
