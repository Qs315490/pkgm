try:
    import requests
except ImportError:
    print("请安装 requests 模块")
    quit(1)
import json


class GithubRepo():
    def __init__(self, repo: str) -> None:
        back = requests.get(
            "https://api.github.com/repos/{}/releases/latest".format(repo))
        json_data = json.loads(back.text)
        self.tag = json_data["tag_name"]
        self.body = json_data["body"]
        downloadUrl = []
        for url in json_data["assets"]:
            downloadUrl.append(
                {"name": url["name"], "url": url["browser_download_url"]})
        self.url = downloadUrl
