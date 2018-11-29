import urllib
import urllib.parse
import urllib.request
import json


def getRepoCount(username):
    url = 'https://api.github.com/users/'
    x = urllib.request.urlopen(url + username)
    data = x.read().decode("utf-8")
    main = json.loads(data)
    return int(main.get("public_repos"))

def getRepoData(username):
    try:
        url = 'https://api.github.com/users/'

        userRepos = []
        userNames = [username]
        mainName = username

        x = urllib.request.urlopen(url + username)
        data = x.read().decode("utf-8")

        main = json.loads(data)

        userRepos.append(getRepoCount(mainName))
        allUsers = main.get("followers_url")

        x = urllib.request.urlopen(allUsers)
        data = x.read().decode("utf-8")
        users = json.loads(data)

        top = len(users)
        if (top > 19):
            top = 19

        for i in range(top):
            name = users[i].get("login")
            userRepos.append(getRepoCount(name))
            userNames.append(name)

        sortedRepo = sorted(userRepos)
        sortedUser = [x for _,x in sorted(zip(userRepos,userNames))]

        colors = []
        data = []
        cats = []
        mainNum = sortedUser.index(mainName)
        for i in range(len(sortedUser)):
            cats+= [str(sortedUser[i])]
            data+= [str(sortedRepo[i])]
            if (i != mainNum):
                colors+=["gray"]
            else:
                colors+=["red"]


        return [cats, colors, data]
    except Exception as e:
        print(e)
a = getRepoData("Marek")
