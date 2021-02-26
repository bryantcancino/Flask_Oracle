import json
import logging
import os
import yaml

class Configuration:

    def __init__(self):
        #self.ssm = boto3.client('ssm')
        self.logger = logging.getLogger()
        os.environ['SPRING_PROFILES_ACTIVE'] = 'local'

    def get_configuration(self):
        content = None
        base_path = os.getcwd() + "/web/"
        filename = "bootstrap.yml"
        document = open(base_path + filename, 'r')
        parsed = yaml.safe_load_all(document)
        python_config = []
        for doc in parsed:
            python_config.append(json.loads(json.dumps(doc)))
        selected = None
        profile_active = os.getenv("SPRING_PROFILES_ACTIVE")
        if profile_active is not None:
            self.logger.info("The selected profile is " + profile_active)
            for i in range(1, len(python_config)):
                if profile_active == python_config[i]['python']['profiles']:
                    selected = i
            if selected is not None:
                if python_config[selected]['connection']['password'] is not None:
                    os.environ['DBAAS_PASSWORD'] = python_config[selected]['connection']['password']
                    
                if python_config[selected]['connection']['user'] is not None:
                    os.environ['DBAAS_USER_NAME'] = python_config[selected]['connection']['user']
                    
                if python_config[selected]['connection']['server'] is not None:
                    os.environ['DBAAS_SERVER'] = python_config[selected]['connection']['server']
                    
                if python_config[selected]['connection']['port'] is not None:
                    os.environ['DBAAS_PORT'] = str(python_config[selected]['connection']['port'])
                    
                if python_config[selected]['connection']['sid'] is not None:
                    os.environ['DBAAS_SID'] = python_config[selected]['connection']['sid']
                
        else:
            self.logger.error("#####ERROR### Could not find a profile active")
        return content
