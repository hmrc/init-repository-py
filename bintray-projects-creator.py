__author__ = 'ck'

import csv
import os
import sys
import requests
from requests.auth import HTTPBasicAuth
import json

bintray_api_root = "https://bintray.com/api/v1"


def read_prop_file(f):
    return dict([(row[0].strip(), row[1].strip()) for row in csv.reader(open(f, 'r'), delimiter='=')])


bintray_props = read_prop_file(os.path.expanduser('~/.bintray/.credentials'))


def create_bintray_repo(repo_name, package_name):
    url = bintray_api_root + "/packages/hmrc/" + repo_name
    git_repo = "https://github.com/hmrc/" + package_name

    print(url)
    payload = {
        "name": package_name,
        "desc": package_name,
        "labels": [],
        "licenses": ["Apache-2.0"],
        "vcs_url": git_repo,
        "website_url": git_repo,
        "issue_tracker_url": git_repo + "/issues",
        "github_repo": "hmrc/" + package_name,
        "github_release_notes_file": "",
        "public_download_numbers": False,
        "public_stats": False
    }

    return requests.post(url,
                         data=json.dumps(payload),
                         auth=HTTPBasicAuth(bintray_props['user'], bintray_props['password']),
                         headers={'content-type': 'application/json'})


def bintray_post(package_name):
    repos = ['releases', 'release-candidates']

    last_response = None

    for repo_name in repos:
        last_response = create_bintray_repo(repo_name, package_name)

        if last_response.status_code != 201:
            return last_response

        print("created " + package_name + " in " + repo_name)

    return last_response


if len(sys.argv) != 2:
    print('usage: new_repo_name')
    sys.exit(-1)

new_repo_name = sys.argv[1]
print('creating %s on bintray' % new_repo_name)

bintray_response = bintray_post(new_repo_name)

if bintray_response.status_code == 201:
    print('successfully created bintray repositories')
else:
    print('failed to create bintray repos with', str(bintray_response.status_code), str(bintray_response.text))
    sys.exit(-1)
