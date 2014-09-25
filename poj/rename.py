from glob import glob
import os
import requests
from bs4 import BeautifulSoup


def get_problem_title(problem_id):
    r = requests.get('http://poj.org/problem?id={}'.format(problem_id))
    soup = BeautifulSoup(r.content)
    return soup.title.string.split(' -- ')[1]


for d in glob("./*"):
    if not os.path.isdir(d):
        continue
    id = d.split('-')[1]
    title = get_problem_title(id)
    title = ''.join(c for c in title.replace(' ', '-') if (c.isalnum() or c in ['-']))
    print(d, 'rename to', '{}-{}'.format(title, id))
    os.rename(d, '{}-{}'.format(title, id))
