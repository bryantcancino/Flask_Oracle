import json
import logging
import os
import yaml

class Configuration:

    def __init__(self):
        self.logger = logging.getLogger()
        base_path = os.getcwd() + "/web/"
        filename = "bootstrap.yml"
        document = open(base_path + filename, 'r')
        parsed = yaml.safe_load_all(document)
        self.python_config = []
        for doc in parsed:
            self.python_config.append(json.loads(json.dumps(doc)))
        selected = None
        app_name = self.python_config[0]['python']['application']['name']
        profile = self.python_config[0]['python']['profiles']['active']
        if profile is None:
            profile = 'local'
        os.environ['SPRING_PROFILES_ACTIVE'] = profile
        self.logger.info("The APP NAME: " + app_name)
        self.logger.info("The selected profile is " + profile)       

    def get_configuration(self):
        process = []

        profile_active = os.getenv("SPRING_PROFILES_ACTIVE")
        if profile_active is not None:
            for i in range(1, len(self.python_config)):
                if profile_active == self.python_config[i]['python']['profiles']:
                    selected = i
            if selected is not None:
                if self.python_config[selected]['server']['port'] is not None:
                    os.environ['SERVER_PORT'] = str(self.python_config[selected]['server']['port'])
                    process.append(os.getenv("SERVER_PORT"))

                if self.python_config[selected]['connection']['password'] is not None:
                    os.environ['DBAAS_PASSWORD'] = self.python_config[selected]['connection']['password']
                    process.append(os.getenv("DBAAS_PASSWORD"))
                    
                if self.python_config[selected]['connection']['user'] is not None:
                    os.environ['DBAAS_USER_NAME'] = self.python_config[selected]['connection']['user']
                    process.append(os.getenv("DBAAS_USER_NAME"))
                    
                if self.python_config[selected]['connection']['server'] is not None:
                    os.environ['DBAAS_SERVER'] = self.python_config[selected]['connection']['server']
                    process.append(os.getenv("DBAAS_SERVER"))
                    
                if self.python_config[selected]['connection']['port'] is not None:
                    os.environ['DBAAS_PORT'] = str(self.python_config[selected]['connection']['port'])
                    process.append(os.getenv("DBAAS_PORT"))
                    
                if self.python_config[selected]['connection']['sid'] is not None:
                    os.environ['DBAAS_SID'] = self.python_config[selected]['connection']['sid']
                    process.append(os.getenv("DBAAS_SID"))
                
        else:
            self.logger.error("#####ERROR### Could not find a profile active")
        self.logger.info("Configurations: "+str(len(process)>=6))
        #app.logger.info("Configurations: "+str(config))              
        #return process
