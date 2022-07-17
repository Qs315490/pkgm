from distutils.command.config import config
from database.config import *


def addRepo(argv):
	argc = len(argv)
	config = openDB()

	if argc < 2:
		print("缺少参数")
		return

	print("正在搜索软件源")
	for repo in config["repo"]:
		if repo["src"] == argv[0]:
			print("已找到软件源")
			print("软件源地址不可重复")
			return

	print("正在添加软件源")
	config["repo"].append({"src": argv[0], "type": argv[1]})
	
	print("正在写出数据")
	writeDB(config)
	print("更新完成")
	quit(0)