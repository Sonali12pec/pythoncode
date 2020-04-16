from git import Repo
repo=Repo('/home/so.garg/example/scrapy')
assert repo.bare == False
repo.remotes.origin.pull()
current = repo.head.commit
repo.remotes.origin.pull()
if current != repo.head.commit:
    print("It changed")