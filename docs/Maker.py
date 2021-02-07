from Project.get_project import GetProject

def maker():
    pjlist = GetProject().get_projects()
    for i in pjlist:
        pname = i["Project"]
        purl = i["Url"]
        oname = i["Owner"]
        repo = i["Repo"]
        ourl = i["Owner_Url"]
        cst = i["Custom_Markdown"]
        repo_u = repo.replace("/","-")
        with open(f"./docs/{repo_u}.md",mode="w",encoding="utf-8") as f:
            md = f"# 项目名 {pname}  \n## 拥有者 [{oname}]({ourl})  \n## 项目地址 [{repo}]({purl})  \n{cst}"      
            f.write(md)

                