import telnetlib
from log import Log, MessageException

import tkinter.messagebox
def show_message(e):
    tkinter.messagebox.showinfo(e.message) 

class Tel:
    def __init__(self, host: str, user: str, pwd: str, user_prompt:str, pass_prompt:str, timeout: int, log: Log = None):
        self.log = log or Log('Tel')
        self.switch_usr = user
        self.switch_pass = pwd
        self.switch_ip = host
        self.user_prompt = user_prompt
        self.pass_prompt = pass_prompt
        self.timeout = timeout

    def connect(self):
        try:
            self.tel = telnetlib.Telnet(self.switch_ip, 23, timeout=2)
        except ConnectionRefusedError as e:
            raise MessageException('Connection refused while connecting to switch, ensure configuration is correct') from e
        except OSError as e:
            raise MessageException('Unknown (most likely connection) issue while connecting to switch') from e
        except Exception as e:
            raise MessageException('Unknown error occured when connecting and logging in to switch') from e
        
        self.login()

    def close_connection(self):
        try:
            return self.tel.close()
        except Exception as e:
            raise MessageException('Exception occured while closing connection...? Please try again') from e

    def login(self): 
        try:
            self.tel.read_until(self.user_prompt.encode('utf-8'), timeout=self.timeout)
            self.tel.write(self.switch_usr.encode('ascii') + b"\n")
            self.tel.read_until(self.pass_prompt.encode('utf-8'), timeout=self.timeout)
            self.tel.write(self.switch_pass.encode('ascii') + b"\n")
        except EOFError as e:
            raise MessageException('Reached timout on login, ensure the pass_prompt and user_prompt and login info is correct') from e
        except OSError as e:
            raise MessageException('Connection was probably close while logging in, please try again') from e
        except Exception as e:
            raise MessageException('Unknown error occured when attempting to login to switch, ensure configuration is correct') from e

    def send(self, command, validation):
        self.connect()

        self.tel.write(command.encode('ascii') + b"\n")
        output = self.tel.read_some().decode('ascii')

        if validation is None:
            return
        
        try: 
            output = self.tel.expect(validation.encode('utf-8'), timeout=self.timeout
                                         ).decode('ascii')
        except EOFError as e:
            raise 

        #output = self.tel.read_all().decode('ascii')

        return output

    def send_command(self, commands, validations):
        for i, (command, validation) in enumerate(zip(commands, validations)):
            try:
                self.send(command, validation)
            except MessageException as e:
                show_message(e)
            except Exception as e:
                raise RuntimeError from e
                
