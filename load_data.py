import github

print('getting repo..')
cowrie_repo = github.Github().get_user('cowrie').get_repo('cowrie')

print('getting pull requests..')
pull_requests = [pull for pull in cowrie_repo.get_pulls()]

print('getting forks..')
forks = [forks for forks in cowrie_repo.get_forks()]

print('names of forkers:')
for fork in forks:
    print(fork.full_name)

