from fileinput import filename


try:
    import yaml
except ImportError:
    print("请安装 pyyaml 模块")
    quit(1)

fileName="config.yml"

def openDB():
	try:
		with open(fileName, "r", encoding="utf-8") as f:
			config = yaml.load(f, Loader=yaml.FullLoader)
	except FileNotFoundError:
		print("无法打开{}文件或文件不存在".format(fileName))
		quit(1)
	return config

def writeDB(newConfig):
	with open(fileName, "w", encoding="utf-8") as f:
		yaml.dump(newConfig, f)
	print("更新完成")