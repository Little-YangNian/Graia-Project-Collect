from Project import get_project
import jinja2



class MakeWeb():
    def __init__(self):
        pass

    def make_web(self, name, url, owner,repo):
        with open('./Web/template.html',encoding='UTF-8') as t:
            template = jinja2.Template(t.read())
            tfs  = template.render(project=name,url=url,owner=owner,repo=repo)
            with open(f'./Web/Collect/{name}.html',mode='w+') as f:
                f.write(tfs)

            

    def get_project_dict(self):
        project_list = get_project.GetProject().get_projects()
        for i in project_list:
            name = i['Project']
            url = i['Url']
            owner = i['Owner']
            repo = i['Repo']
            self.make_web(name, url, owner,repo)
    def run(self):
        self.get_project_dict()
