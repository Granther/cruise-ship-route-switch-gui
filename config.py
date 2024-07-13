import xml.etree.ElementTree as ET
from log import Log, LogException

class ConfigFileException(LogException):
    def __init__(self, message):
        super().__init__(message)

class ConfigPermissionException(LogException):
    def __init__(self, message):
        super().__init__(message)

class ConfigException(LogException):
    def __init__(self, message):
        super().__init__(message)

class Config:
    def __init__(self):
        self.log = Log('Config')
        self.routes = []

        try:
            self.find_config()
        except (ConfigFileException, ConfigPermissionException):
            try:
                self.generate_config()
            except (ConfigFileException, ConfigPermissionException) as e:
                raise ConfigException(f'Unable to read/access config file {self.configPath}') from e
            
        self.read_config()

    def handle_route_prof(self, route):
        commands = []
        validation = []

        for step in route:
            commands.append(step[0].text if not '' else None)
            validation.append(step[1].text if not '' else None)

        routeProf = RouteProfile(route.tag, commands, validation)

        self.routes.append(routeProf)

        return


    def read_config(self):
        if self.configPath == None:
            self.log.write_log('here')
            self.log.write_log(f'ERROR: Unable to parse {self.configPath}, using hard coded Config. I DO NOT RECOMMEND THIS!!')

        #try:
        tree = ET.parse(self.configPath)
        root = tree.getroot()

        self.switch_usr = root[0].text
        self.switch_pass = root[1].text
        self.user_prompt = root[2].text
        self.pass_prompt = root[3].text
        self.switch_ip = root[4].text

        self.test = root.find('routes')

        for route in self.test:
            self.handle_route_prof(route)

        #except:
        #    self.log.write_log(f'ERROR: Unable to parse {self.configPath}, using hard coded Config. I DO NOT RECOMMEND THIS!!')            

    def find_config(self):
        try:
            self.configPath = 'config.xml'
            file = open(self.configPath, 'r')
        except FileNotFoundError as e:
            raise ConfigFileException(f'Exception raised when locating {self.configPath} for instantiation') from e
        except PermissionError as e:
            raise ConfigPermissionException(f'User lacks permissions to read {self.configPath}') from e
        except Exception as e:
            raise ConfigFileException(f'Exception occured when finding config {self.configPath}') from e

    def generate_config(self):
        try:
            self.configPath = 'config.xml'
            file = open(self.configPath, 'wr')
            file.write(self.config_template)
            file.close()
            self.log.write_log(f'Generated config file from {self.configPath}')
        except PermissionError as e:
            raise ConfigPermissionException(f'User lacks permissions to read/write {self.configPath}') from e
        except Exception as e:
            raise ConfigFileException(f'Exception occured when creating config {self.configPath}') from e


class RouteProfile():
    def __init__(self, name, command_list, validation_list):
        self.name = name
        self.command_list = command_list
        self.validation_list = validation_list
