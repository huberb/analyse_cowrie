import github
import pickle
from creds import name, pw

print('getting repo..')
cowrie_repo = github.Github(name(), pw()).get_user('cowrie').get_repo('cowrie')

print('getting pull requests..')
pull_requests = [pull for pull in cowrie_repo.get_pulls('all')]

print('getting forks..')
forks = [forks for forks in cowrie_repo.get_forks()]

with open('pull_requests', 'wb') as f:
    pickle.dump(pull_requests, f)
with open('forks', 'wb') as f:
    pickle.dump(forks, f)
