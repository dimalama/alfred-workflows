# Alfred Workflows for GitHub Search

This repository contains two powerful Alfred workflows that enhance your GitHub search experience:

## 1. GitHub Project Search (`github-project-search`)

A workflow designed for searching through your personal GitHub repositories and collaborations.

### Key Features:
- Search through repositories you own or collaborate on
- Search by repository names and descriptions
- Shows repository visibility (public/private)
- Sorted by best match and recency
- Quick access via `ghs` keyword

## 2. GitHub Organization Project Search (`github-org-project-search`)

A workflow specifically built for searching through repositories within your GitHub organization.

### Key Features:
- Search across all repositories in your organization
- Shows up to 100 most recently updated repositories
- Search through repository names and descriptions
- Quick access via `gos` keyword

## Prerequisites

- Alfred with Powerpack
- Python 3
- GitHub Personal Access Token
- For org search: Access to a GitHub organization

## Installation & Setup

Both workflows require similar setup steps:

1. Download the desired `.alfredworkflow` file
2. Double-click to install in Alfred
3. Configure GitHub token:
   - Go to GitHub Settings → Developer Settings → Personal Access Tokens
   - Generate a new token with `repo` scope
   - Add token to workflow settings as `GITHUB_TOKEN`
4. For org search: Set your `ORG_NAME` in workflow settings

## License

MIT License

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.