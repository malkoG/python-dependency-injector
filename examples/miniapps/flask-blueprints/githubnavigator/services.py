"""Services module."""

from github import Github
from github.Repository import Repository
from github.Commit import Commit


# [TODO] SearchService
class SearchService:
    """Search service performs search on Github."""

    # [TODO] SearchService > __init__
    def __init__(self, github_client: Github):
        self._github_client = github_client

    # [TODO] SearchService > search_repositories
    def search_repositories(self, query, limit):
        """Search for repositories and return formatted data."""
        repositories = self._github_client.search_repositories(
            query=query,
            **{"in": "name"},
        )
        return [
            self._format_repo(repository)
            for repository in repositories[:limit]
        ]

    # [TODO] SearchService > _format_repo
    def _format_repo(self, repository: Repository):
        commits = repository.get_commits()
        return {
            "url": repository.html_url,
            "name": repository.name,
            "owner": {
                "login": repository.owner.login,
                "url": repository.owner.html_url,
                "avatar_url": repository.owner.avatar_url,
            },
            "latest_commit": self._format_commit(commits[0]) if commits else {},
        }

    # [TODO] SearchService > _format_commit
    def _format_commit(self, commit: Commit):
        return {
            "sha": commit.sha,
            "url": commit.html_url,
            "message": commit.commit.message,
            "author_name": commit.commit.author.name,
        }