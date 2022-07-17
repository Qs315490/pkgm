from database.pkgdb import writeDB
from database.config import openDB


def update(args):
    config = openDB()
    pkgdb = []
    for repo in config["repo"]:
        if len(args) > 0:
            if repo["src"] not in args:
                continue
        try:
            repoEnable = repo["enable"]
        except:
            repoEnable = True
        if repoEnable == False:
            continue
        if repo["type"] == "github":
            print("pkg: {}".format(repo["src"]))  # 打印软件包名称
            from repo.github import GithubRepo
            try:
                pkg = GithubRepo(repo["src"])
            except:
                # 跳过产生错误的软件包
                print("无法获取 Github 仓库信息")
                continue
            print("ver: {}\n".format(pkg.tag))  # 打印最新版本
            pkgdb.append(
                {"name": repo["src"],
                 "ver": pkg.tag,
                 "desc": pkg.body,
                 "url": pkg.url})

    print("正在写出数据")
    writeDB(pkgdb)
    print("更新完成")
