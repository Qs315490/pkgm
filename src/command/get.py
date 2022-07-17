from distutils.command.config import config
import database.pkgdb as pkgDB
import database.config as conf
import re

downloadFlag = 0


def get(pkgName, flag=0):
    if flag != 0:
        global downloadFlag
        downloadFlag = flag

    for package in pkgName:
        getPackage(package)


def getPackage(repoPackage):
    print("正在从本地存储库中查找软件包")
    pkgdb = pkgDB.openDB()

    # 遍历pkgdb，查找匹配的软件包
    for pkg in pkgdb:
        # 判断软件包名称是否与本地存储库中项目匹配
        if pkg["name"] == repoPackage:
            print("软件包已找到")

            # 获取软件包的下载地址
            url = pkg["url"]
            urlCount = len(url)
            if urlCount == 0:
                print("软件包没有下载地址")
                quit(1)
            elif urlCount == 1:
                download(url[0]["name"], url[0]["url"])
            else:  # 多文件选择下载
                # 查找配置文件是否指定下载文件
                config = conf.openDB()
                # 配置文件中指定下载文件
                for pkgConfig in config["repo"]:  # 遍历配置文件
                    # 判断配置文件中的软件包名称是否与本地存储库中项目匹配
                    if pkgConfig["src"] == repoPackage:
                        # 遍历本地存储库中软件包的文件列表
                        for pkgindex in range(len(url)):
                            # 判断配置文件指定名称是否与本地存储库中项目匹配
                            try:
                                customFile = pkgConfig["file"]
                            except:
                                continue
                            else:
                                if re.search(customFile, url[pkgindex]["name"]) is not None:
                                    download(url[pkgindex]["name"],
                                                url[pkgindex]["url"])
                                    return
                # 未指定下载文件
                for pkgindex in range(len(url)):
                    print("{}. {}".format(pkgindex, url[pkgindex]["name"]))
                userInput = input("请输入要下载的软件包下载序号: ")
                if userInput.isdigit():
                    pkgindex = int(userInput)
                    if pkgindex < len(url):
                        download(url[pkgindex]["name"], url[pkgindex]["url"])
                        return
                    else:
                        print("输入的序号超出范围")
                        quit(1)
                else:
                    print("输入的序号不是数字")
                    quit(1)


def download(pkgName, url):
    def downloadPkg():
        print("正在下载 {}".format(pkgName))
        # TODO: 实现下载
    if downloadFlag == 0:  # 询问
        print(
            "是否下载 {} y/N?".format(pkgName))
        userInput = input()
        if userInput == "y":
            downloadPkg()
    elif downloadFlag == 1:  # 默认允许
        downloadPkg()
    else:  # 不允许
        print("已取消下载 {}".format(pkgName))
    return
