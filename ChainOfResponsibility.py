# Developer: TUBUN JANA
# Company: --------------
# Project: Logging System with Chain of Responsibility Pattern
# Description: This script demonstrates the use of the Chain of Responsibility design pattern
#              to handle different log levels (INFO, DEBUG, ERROR) using a chain of log handlers.
#              The handlers process specific log levels and pass requests to the next handler
#              if they are not able to process the request themselves.
# Date: January 1, 2025
# Version: 1.0

from abc import ABC, abstractmethod
from enum import Enum

# Enum class to represent different log levels
# This is an industry-standard approach to manage log levels like INFO, DEBUG, ERROR, and UNKNOWN.
# In logging systems, these levels are typically used to categorize and control the verbosity of logs.
class LogsEnum(Enum):
    INFO = "info"
    DEBUG = "debug"
    ERROR = "error"
    UNKNOWN = "unknown"

# Abstract Handler class (Chain of Responsibility pattern)
# This class defines the common interface for all concrete log handlers (InfoLoggHandler, ErrorLoggHandler, DebugLoggHandler).
# It also contains the logic to pass the request down to the next handler in the chain if it cannot process the request.
class LoggHandler(ABC):
    def __init__(self, next_handler: "LoggHandler" = None):
        self._next_handler = next_handler  # Linking the next handler in the chain
    
    @abstractmethod
    def handleRequest(self, request: str):
        pass  # This will be implemented by concrete handlers

# Concrete handler for INFO level logs
# This handler will handle log requests that are of INFO level. 
# If the request cannot be handled (i.e., it's not INFO), it passes the request down the chain to the next handler.
class InfoLoggHandler(LoggHandler):
    def __init__(self, next_handler: LoggHandler = None):
        super().__init__(next_handler=next_handler)
    
    def handleRequest(self, request: str):
        if request == LogsEnum.INFO:
            print("Your request handled by InfoLoggHandler class.")
        elif self._next_handler:
            print(f"Your request sent to {self._next_handler.__class__.__name__}")
            self._next_handler.handleRequest(request=request)
        else:
            print(f"Your request is stopped in the InfoLoggHandler")

# Concrete handler for ERROR level logs
# This handler specifically deals with ERROR level log requests.
# If the request is not ERROR, it forwards it to the next handler in the chain (if any).
class ErrorLoggHandler(LoggHandler):
    def __init__(self, next_handler: LoggHandler = None):
        super().__init__(next_handler=next_handler)
    
    def handleRequest(self, request: str):
        if request == LogsEnum.ERROR:
            print("Your request handled by ErrorLoggHandler class.")
        elif self._next_handler:
            print(f"Your request sent to {self._next_handler.__class__.__name__}")
            self._next_handler.handleRequest(request=request)
        else:
            print(f"Your request is stopped in the ErrorLoggHandler")

# Concrete handler for DEBUG level logs
# Handles DEBUG level log requests.
# If it's not a DEBUG request, it passes the request to the next handler.
class DebugLoggHandler(LoggHandler):
    def __init__(self, next_handler: LoggHandler = None):
        super().__init__(next_handler=next_handler)
    
    def handleRequest(self, request: str):
        if request == LogsEnum.DEBUG:
            print("Your request handled by DebugLoggHandler class.")
        elif self._next_handler:
            print(f"Your request sent to {self._next_handler.__class__.__name__}")
            self._next_handler.handleRequest(request=request)
        else:
            print(f"Your request is stopped in the DebugLoggHandler")

# Main function simulating a real-world logging system with Chain of Responsibility pattern
# The handlers are set up in a chain where:
# - Debug logs are handled by DebugLoggHandler,
# - Info logs are handled by InfoLoggHandler,
# - Error logs are handled by ErrorLoggHandler.
# In case a log request cannot be handled by the current handler, it is passed to the next handler in the chain.
if __name__ == "__main__":
    # Creating the chain of responsibility (handlers)
    error = ErrorLoggHandler()  # The last handler in the chain (handles ERROR logs)
    info = InfoLoggHandler(next_handler=error)  # Handles INFO logs, forwards to error handler if needed
    debug = DebugLoggHandler(next_handler=info)  # Handles DEBUG logs, forwards to info handler if needed
    
    # Test requests that trigger different handlers
    debug.handleRequest(request=LogsEnum.ERROR)  # Triggers ErrorLoggHandler
    print("\n")
    debug.handleRequest(request=LogsEnum.INFO)   # Triggers InfoLoggHandler
    print("\n")
    debug.handleRequest(request=LogsEnum.DEBUG)  # Triggers DebugLoggHandler
    print("\n")
    debug.handleRequest(request=LogsEnum.UNKNOWN)  # No handler can process this, stops in DebugLoggHandler
