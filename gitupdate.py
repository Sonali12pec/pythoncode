
# TODO : Start using shebang statement
# https://stackoverflow.com/questions/6908143/should-i-put-shebang-in-python-scripts-and-what-form-should-it-take

from git import Repo

# TODO
# the problem statement was to update the git repo in current directory, but you are hardcoding the path here
# also the path you hardcoded does not exist on system of user, so the script is useless for user
# you could've provided the facility to provide path from outside as well
repo=Repo('/home/so.garg/example/scrapy')
assert repo.bare == False
repo.remotes.origin.pull()
current = repo.head.commit
repo.remotes.origin.pull()
if current != repo.head.commit:
    print("It changed")
