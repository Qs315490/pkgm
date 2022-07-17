from database.config import *


def setRepo(argv):
    config = openDB()

    argc = len(argv)
    if argc <= 1:
        print("缺少参数")
        return

    print("正在搜索软件源")
    try:
        for repo in config["repo"]:
            if repo["src"] == argv[0]:
                print("已找到软件源")
                if argc == 3:
                    repo[argv[1]] = argv[2]
                    print("设置成功")
                    break
                else:
                    print(argv[1]+":", repo[argv[1]])
                    return
    except KeyError:
        print("参数错误")
        return

    print("正在写出数据")
    writeDB(config)
    print("更新完成")
    quit(0)
