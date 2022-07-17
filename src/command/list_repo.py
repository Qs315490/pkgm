from distutils.command.config import config
from database.config import openDB


def listRepo():
    config = openDB()
    for repo in config["repo"]:
        print("名称：", repo["src"])
        print("类型：", repo["type"])
        try:
            enable = repo["enable"]
        except:
            enable = True
        print("是否启用：", enable)
        try:
            customFile = repo["file"]
        except:
            customFile = None
        if customFile is not None:
            print("指定文件：", customFile)
        print()
