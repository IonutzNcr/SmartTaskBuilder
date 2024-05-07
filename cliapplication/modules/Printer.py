from abc import ABC, abstractmethod
from ColorCli import Colors

class PrinterInterface(ABC):
    @abstractmethod
    def print_system_message(cls, message: str) -> None:
        pass
    
    @abstractmethod
    def print_error_message(cls, message: str) -> None:
        pass
    
    @abstractmethod
    def print_debug_message(cls, message: str) -> None:
        pass
    

class Printer(PrinterInterface):
    @classmethod
    def print_system_message(cls, message: str) -> None:
        print(Colors.WARNING + message + Colors.ENDC)
        
    @classmethod
    def print_error_message(cls, message: str) -> None:
        print(Colors.FAIL + message + Colors.ENDC)
        
    @classmethod
    def print_debug_message(cls, message: str) -> None:
        print(Colors.OKBLUE)
        print(message)
        print(Colors.ENDC)