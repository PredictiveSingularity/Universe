#!/usr/bin/bash

# This script is used to fetch the docs from the remote to the local machine.

echo "Initializing docs repos"
mkdir -p _build

repo_docs=(
    "ursina https://github.com/pokepetter/ursina.git"
)

echo "Fetching docs repos"
for repo in "${repo_docs[@]}"; do
    repo_name=$(echo $repo | cut -d' ' -f1)
    repo_url=$(echo $repo | cut -d' ' -f2)
    echo "Fetching $repo_name"
    git clone $repo_url _build/$repo_name

    # if docs folder exists in the repo copy it ro the docs folder
    if [ -d _build/$repo_name/docs ]; then
        # Make sure to remove the docs folder if it exists
        if [ -d -/$repo_name ]; then
            rm -rf ./$repo_name
        fi

        echo "Copying docs for $repo_name..."
        cp -r _build/$repo_name/docs ./$repo_name
        echo "Updated docs for $repo_name"
    fi
done

echo "Removing docs repos"
rm -rf _build/*
rmdir _build

echo "Fetching docs complete"