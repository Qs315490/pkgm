from distutils.command.config import config
from database.config import *


def delRepo(repoName):
	config = openDB()
	print("正在搜索软件源")
	for repo in config["repo"]:
		if repoName == repo["src"]:
			userInput = input("确定删除软件源？(y/N)")
			if userInput == "y":
				config["repo"].remove(repo)
				print("软件源已删除")
				break
			else:
				print("已取消删除")
				break

	print("正在写出数据")
	writeDB(config)
	print("更新完成")