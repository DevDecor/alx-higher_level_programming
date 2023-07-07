#!/usr/bin/python3
"""Python script that takes 2 arguments in order to list
10 commits"""
import sys
import requests


if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    for commit in requests.get(url).json()[:10]:
        print(f"{commit['sha']}: {commit['commit']['committer']['name']}")
