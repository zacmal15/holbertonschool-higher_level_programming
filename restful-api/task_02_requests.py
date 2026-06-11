#!/usr/bin/python3
"""Fetch posts from an API and save selected data to CSV."""

import csv
import requests


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print each post title."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save them to posts.csv."""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        data = []
        for post in posts:
            data.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
