#!/bin/bash
set -e

# Only act if this is build was fired from a push to master.
if [ "${TRAVIS_PULL_REQUEST}" = "false" ] && [ "${TRAVIS_TAG}" = "false" ] && [ "${TRAVIS_BRANCH}" = "master" ]
then
    # Configure git user.
    setup_git() {
        git config --global user.email "deploy@travis-ci.org"
        git config --global user.name "Deployment Bot"
    }
    
    # Commit all changes to local production branch.
    commit_all_files() {
        git checkout -b production
        git add -A
        git commit --message "Travis Build: ${TRAVIS_BUILD_NUMBER}"
    }
    
    # Push changes to remote production branch.
    push_files() {
        git remote add origin https://${gh_bot_token}@github.com/WikipediaLibrary/TWLight.git > /dev/null 2>&1
        git push --quiet --set-upstream origin production
    }

    setup_git
    commit_all_files
    push_files
    echo "Build pushed to production."
else
    echo "Doesn't meet conditions for deployment. Skipping push to production."
fi