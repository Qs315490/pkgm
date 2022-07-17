import sys

args = sys.argv[1:]
argc = len(args)
if argc > 0:
    if args[0] == "update" or args[0] == 'u':
        # 更新本地存储库
        if "-h" in args:
            args.remove("-h")
            print("""
update [指定软件源[ 指定软件源1 ...]]
更新本地存储库. 如果没有指定软件源，则更新所有软件源.
------------
-h: 显示帮助
------------

""")
            quit(0)
        from command.update import update
        update(args[1:])
        quit(0)
    if args[0] == "upgrade" or args[0] == 'ug':
        # 更新本地软件包
        pass
    if args[0] == "get" or args[0] == 'g':
        # 下载软件包文件
        flag = 0
        if "-y" in args:
            args.remove("-y")
            flag = 1
        if "-n" in args:
            args.remove("-n")
            flag = 2
        if "-h" in args:
            args.remove("-h")
            print("""
get [指定软件包名[ 指定软件包名1 ...]]
下载所选软件包文件.
------------
-y: 自动确认下载
-n: 取消下载
-h: 查看帮助
------------

""")
            quit(0)
        if argc >= 2:
            from command.get import get
            get(args[1:], flag)
        else:
            print("请输入软件包名称")
            quit(1)
        quit(0)
    if args[0] == "add" or args[0] == 'a':
        # 安装软件包
        # TODO: 安装软件包
        quit(0)
    if args[0] == "del" or args[0] == 'd':
        # 删除软件包
        # TODO: 删除软件包
        quit(0)
    if args[0] == "search" or args[0] == 's':
        # 搜索软件包
        if "-h" in args:
            args.remove("-h")
            print("""
search 指定关键字
搜索软件包. 关键字可以是软件包名称、软件包作者. 
------------
-h: 查看帮助
------------

""")
            quit(0)
        if argc >= 2:
            from command.search import search
            search(args[1])
        else:
            print("请输入要搜索的关键字")
            quit(1)
        quit(0)
    if args[0] == "info" or args[0] == 'i':
        # 查看软件包信息
        if "-h" in args:
            args.remove("-h")
            print("""
info [指定软件包名]
查看软件包信息. 如果没有指定软件包名，则查看所有软件包.
------------
-h: 查看帮助
------------

""")
            quit(0)
        if argc >= 2:
            from command.info import info
            info(args[1])
        else:
            print("请输入要查看的软件包名称")
            quit(1)
        quit(0)
    if args[0] == "list" or args[0] == 'l':
        # 已安装软件包列表
        # TODO: 已安装软件包列表
        quit(0)
    if args[0] == "list-command" or args[0] == 'lr':
        # 已安装软件源列表
        if "-h" in args:
            args.remove("-h")
            print("""
list-command
查看已安装软件源列表.
------------
-h: 查看帮助
------------

""")
            quit(0)
        from command.list_repo import listRepo
        listRepo()
        quit(0)
    if args[0] == "addrepo" or args[0] == 'ar':
        # 添加软件源
        if "-h" in args:
            args.remove("-h")
            print("""
addrepo 软件源地址 软件源类型
添加软件源.
------------
-h: 查看帮助
------------

""")
            quit(0)
        if argc >= 3:
            from command.addRepo import addRepo
            addRepo(args[1:])
        else:
            print("请输入软件源地址和软件源类型")
            quit(1)
        quit(0)
    if args[0] == "delrepo" or args[0] == 'dr':
        # 删除软件源
        if "-h" in args:
            args.remove("-h")
            print("""
delrepo 软件源名称
删除软件源.
------------
-h: 查看帮助
------------

""")
        from command.delRepo import delRepo
        delRepo(args[1])
        quit(0)
    if args[0] == "setrepo" or args[0] == 'sr':
        # 设置软件源状态
        if "-h" in args:
            args.remove("-h")
            print("""
setrepo 软件源地址 配置项 [配置值]
设置软件源状态.
------------
-h: 查看帮助
------------

""")
            quit(0)
        if argc >= 2:
            from command.setRepo import setRepo
            setRepo(args[1:])
        else:
            print("缺少参数")
            quit(1)
        quit(0)

print("""
使用方法: {0} 命令 [参数] ...
------------
命令:
------------
    u  update: 更新本地存储库
    ug uparuge: 更新本地软件包
    g  get: 下载软件包文件
    a  add: 安装软件包
    d  del: 删除软件包
    s  search: 搜索软件包
    i  info: 查看软件包信息
    l  list: 已安装软件包列表
    lr list-command: 已安装软件源列表
    ar addrepo: 添加软件源
    dr delrepo: 删除软件源
    sr setrepo: 设置软件源状态
------------
使用命令以查看更多使用方法,列如: {0} update -h
""".format(sys.argv[0]))
