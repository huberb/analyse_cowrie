import pickle
import github

with open('forks', 'rb') as f:
    forks = pickle.load(f)

with open('pull_requests', 'rb') as f:
    pull_requests = pickle.load(f)

print('forks: ')
print(len(forks))

print('pull_requests: ')
print(len(pull_requests))

print('creation date of fork 0:')
print(str(forks[0].created_at))

print('creation date of pull_request 0:')
print(str(pull_requests[0].created_at))

for fork in forks:
    name = fork.owner.login
    pulls = [pull for pull in pull_requests if pull.user.login == name]
    after_pulls = [pull for pull in pull_requests if pull.user.login == name and pull.created_at < fork.created_at]
    before_pulls = [pull for pull in pull_requests if pull.user.login == name and pull.created_at > fork.created_at]

    if len(pulls) > 0:
        print('name: ' + name)
        print('forks after pull request:')
        print(len(after_pulls))
        print()
        print('forks before pull request:')
        print(len(before_pulls))
        print()

import code; code.interact(local=dict(globals(), **locals()))
