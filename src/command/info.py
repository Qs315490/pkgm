from database.pkgdb import openDB


def info(packages):
    pkgdb = openDB()
    for pkg in pkgdb:
        if pkg["name"] in packages:
            print("软件包名称：", pkg["name"])
            print("软件包版本：", pkg["ver"])
            print("软件包描述：\n"+pkg["desc"])
