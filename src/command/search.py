from database.pkgdb import *


def search(package: str):
    pkgdb=openDB()
    for pkginfo in pkgdb:
        if package.lower() in pkginfo["name"].lower():
            print(pkginfo["name"], pkginfo["ver"])
