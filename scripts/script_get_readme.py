from github import Github
import urllib
import os

token = os.environ['AUTH_TOKEN']

g = Github(token)
org = g.get_organization('unbgames')

for repo in org.get_repos():
    try:
        file_content = repo.get_file_contents('unbgames.md')

        if(repo.name != 'unbgames'):
            urllib.request.urlretrieve(file_content.download_url, ('readmes/'+repo.name + '.md'))

    except Exception as e :
        print("Repository: " + repo.name + " don't have readme.md file.")
        print(str(e))
