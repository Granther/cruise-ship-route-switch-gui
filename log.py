import os

class LogException(Exception):
    def __init__(self, message):
        log = Log(self.__class__.__name__, message)
        super().__init__(message)

class LogGeneralException(LogException):
    def __init__(self, message):
        super().__init__(message)

class TelConnectionException(LogException):
    def __init__(self, message):
        super().__init__(message)

class Log:
    def __init__(self, className: str, hotLog = None):
        try:
            self.find_logfile()
        except Exception as e:
            print(f'ERROR: Error encountered while instantiating logs: {e}')
            return None
        
        self.className = className

        if hotLog:
            self.write_log(hotLog)

    def find_logfile(self):
        
        self.logfile = 'logs.txt'
        
        return True
    
    def write_log(self, log):
        try:
            file = open(self.logfile, 'a')
            file.write(f'{self.className}: {log}\n')
            file.close()
        except:
            return False
        
        return True
    
