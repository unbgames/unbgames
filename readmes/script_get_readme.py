from github import Github
import urllib

token = "500aeede18cbe164af9f41b40ce3c7cb98028eb9"

g = Github("Digite o token aqui ou coloque suas credenciais! ") #(user, pass)

org = g.get_organization('plataformagames')

for repo in org.get_repos():
    try:
        file_content = repo.get_file_contents('README.md')
        
        if(repo.name != 'unbgames'):
            urllib.request.urlretrieve(file_content.download_url, ('readmes/'+repo.name + '.md'))
        
    except:
        print("Repository: " + repo.name + " don't have readme.md file.")

