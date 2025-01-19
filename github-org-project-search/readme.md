# GitHub Organization Project Search

An Alfred workflow that allows you to quickly search through all repositories in your GitHub organization.

## Features

- Fast search through all repositories in your GitHub organization
- Searches both repository names and descriptions
- Shows up to 100 most recently updated repositories
- Direct links to repository URLs

## Prerequisites

- Alfred with Powerpack
- Python 3
- GitHub Personal Access Token
- Access to a GitHub organization

## Installation

1. Download the `Github Org Project Search.alfredworkflow` file
2. Double-click to install in Alfred
3. Configure the required environment variables:
   - `GITHUB_TOKEN`: Your GitHub Personal Access Token
   - `ORG_NAME`: Your GitHub organization name

### Setting up GitHub Token

1. Go to GitHub Settings > Developer Settings > Personal Access Tokens
2. Generate a new token with `repo` scope
3. Copy the token and set it as the `GITHUB_TOKEN` environment variable in the workflow settings

## Usage

1. In Alfred, type your workflow keyword (default: `gos`) followed by your search term
2. Results will show matching repositories from your organization
3. Select a repository to open it in your default browser

## Troubleshooting

If you encounter any issues:
- Verify your GitHub token has the correct permissions
- Check that your organization name is correctly set
- Ensure you have access to the organization repositories

## License

MIT License