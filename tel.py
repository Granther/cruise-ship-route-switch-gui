import telnetlib
from config import Config
from log import Log, TelConnectionException

class Tel:
    def __init__(self, host: str, user: str, pwd: str, user_prompt:str, pass_prompt:str, log: Log = None):
        self.log = log or Log('Tel')
        self.switch_usr = user
        self.switch_pass = pwd
        self.switch_ip = host
        self.user_prompt = user_prompt
        self.pass_prompt = pass_prompt

        self.connect()
        self.login()

    def connect(self):
        try:
            self.tel = telnetlib.Telnet(self.switch_ip, 23, timeout=2)
        except ConnectionRefusedError as e:
            raise TelConnectionException from e
        except Exception as e:
            raise RuntimeError from e

    def login(self): 
        self.tel.read_until(self.user_prompt.encode('utf-8'))
        self.tel.write(self.switch_usr.encode('ascii') + b"\n")
        self.tel.read_until(self.pass_prompt.encode('utf-8'))
        self.tel.write(self.switch_pass.encode('ascii') + b"\n")
        # need some err handling here

    def send(self, command, validation):
        self.tel.write(command.encode('ascii') + b"\n")
        #print(self.tel.read_some(b"[grant@rocky-x1 glorptown]$").decode('ascii'))

        if validation is None:
            return
        
        try: 
            output = self.tel.expect(validation.encode('utf-8'), timeout=2
                                         ).decode('ascii')
        except Exception as e:
            print('Unable to end file')

        output = self.tel.read_all().decode('ascii')

        return output

        # catch timeout here

    def send_command(self, commands, validations):
        for i, (command, validation) in enumerate(zip(commands, validations)):
            print(i, command, validation)
            print(self.send(command, validation))

    def starlink(self):
        print(self.connect())

    def att(self):
        pass

# Read config and attempt connection to switch
# Catch errors connecting to switch
# Login
# Catch errors associated with entering text
# read how the switch responds 