"""This is a logging library"""
import time

LOG_FILE = "run.log"

class Logger:
    """Logger, outputs nothing when called. Parent class to other loggers"""
    def _message(self, level, msg):
        """Formulates message"""
        return f"[{time.time()}] [{level}] {msg}"
    def error(self, msg):
        """error"""
        self._output(self._message("ERROR", msg))
    def warn(self, msg):
        """warn"""
        self._output(self._message("WARN", msg))
    def info(self, msg):
        """info"""
        self._output(self._message("INFO", msg))
    def _output(self, msg):
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
    def _output(self, msg):
        """Output"""
        print(msg)

class FileLogger(Logger):
    """Logger that outputs to file"""
    def _output(self, msg):
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f'{msg}\n')

class FileTerminalLogger(Logger):
    """logger that outputs to both File and Terminal"""
    def _output(self, msg):
        with open(LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f'{msg}\n')
        print(msg)

_log_class = DummyLogger()

def mode_update(new_mode):
    """Updates the logger module mode"""
    global _log_class
    if new_mode == "disabled":
        _log_class = DummyLogger()

    elif new_mode == "terminal":
        _log_class = TerminalLogger()

    elif new_mode == "file":
        _log_class = FileLogger()

    elif new_mode == "file_terminal":
        _log_class = FileTerminalLogger()

    else:
        raise ValueError(f"Valid Modes are 'disabled', 'terminal' 'file' and\
                'file_terminal'. Mode recived was {new_mode}")

def error(msg):
    """Allows program to call error through module"""
    _log_class.error(msg)
def warn(msg):
    """Allows program to call warn through module"""
    _log_class.warn(msg)
def info(msg):
    """Allows program to call info through module"""
    _log_class.info(msg)
