from Project.get_project import GetProject
import os

def maker():
    pjlist = GetProject().get_projects()
    for i in pjlist:
        pname = i["Project"]
        purl = i["Url"]
        oname = i["Owner"]
        repo = i["Repo"]
        ourl = i["Owner_Url"]
        cst = i["Custom_Markdown"]
        for i in os.listdir("./docs"):
            q = 1
            q += 1
        with open(f"./docs/{q+1}.md",mode="w",encoding="utf-8") as f:
            md = f"# 项目名 {pname}  \n## 拥有者 [{oname}]({ourl})  \n## 项目地址 [{repo}]({purl})  \n{cst}"      
            f.write(md)

                
