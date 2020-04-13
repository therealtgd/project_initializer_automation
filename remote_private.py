import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = os.environ.get('mp')         # add projects directory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
_dir = path + '/' + foldername

g = Github(token)
user = g.get_user()
login = user.login
repo = user.create_repo(foldername, private=True)

commands = [f'echo "# {repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master']


os.mkdir(_dir)
os.chdir(_dir)
try:
    for c in commands:
        os.system(c)

    print(f'{foldername} created locally')
    os.system('pycharm .')

except:
    print("create <foldername> -p")
