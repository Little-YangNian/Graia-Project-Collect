
import yaml
import os

from yaml.loader import SafeLoader


class GetProject():
    '''Get Files in Projects then Change them to dict'''

    def __init__(self):
            pass
    def get_projects(self):

        files = os.listdir('./Project/Projects')
        project_yml = []
        for i in files:
            with open(f'./Project/Projects/{i}',encoding='utf-8') as f:
                yml = yaml.load(f.read(), Loader=SafeLoader)
                project_yml.append(yml)
            return project_yml
