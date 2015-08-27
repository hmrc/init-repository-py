__author__ = 'ck'

import csv
import os
import sys
import json

import requests
from requests.auth import HTTPBasicAuth

bintray_api_root = "https://bintray.com/api/v1"


def read_prop_file(f):
    return dict([(row[0].strip(), row[1].strip()) for row in csv.reader(open(f, 'r'), delimiter='=')])


def create_package(repo_name, package_name):
    bintray_url = bintray_api_root + "/packages/hmrc/" + repo_name
    git_repository = "https://github.com/hmrc/" + package_name

    bintray_props = read_prop_file(os.path.expanduser('~/.bintray/.credentials'))

    payload = {
        "name": package_name,
        "desc": package_name + " " + repo_name,
        "labels": [],
        "licenses": ["Apache-2.0"],
        "vcs_url": git_repository,
        "website_url": git_repository,
        "issue_tracker_url": git_repository + "/issues",
        "github_repo": "hmrc/" + package_name,
        "public_download_numbers": True,
        "public_stats": True
    }

    return requests.post(bintray_url,
                         data=json.dumps(payload),
                         auth=HTTPBasicAuth(bintray_props['user'], bintray_props['password']),
                         headers={'content-type': 'application/json'})


def create_packages(package_name):
    repo_names = ['releases', 'release-candidates']

    last_response = None

    for repo_name in repo_names:
        last_response = create_package(repo_name, package_name)

        if last_response.status_code != 201:
            return last_response

        print("created " + package_name + " in " + repo_name)

    return last_response

def check_exists_on_github(repository):
    return requests.head("https://github.com/hmrc/" + repository)

if len(sys.argv) != 2:
    print('usage: repository')
    sys.exit(-1)

new_repository = sys.argv[1]

print('checking github repository exists')

github_response = check_exists_on_github(new_repository)
if github_response.status_code == 404:
    print('failed to find github repository')
    sys.exit(-1)

print('creating %s on bintray' % new_repository)

bintray_response = create_packages(new_repository)
if bintray_response.status_code == 201:
    print('successfully created bintray repositories')
else:
    print('failed to create bintray repositories with', str(bintray_response.status_code), str(bintray_response.text))
    sys.exit(-1)
