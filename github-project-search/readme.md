# GitHub Project Search - Alfred Workflow

An Alfred workflow that allows you to quickly search through your GitHub repositories. This workflow helps you find repositories you own or collaborate on, making it easier to access your GitHub projects directly from Alfred.

## Features

- Fast search through your GitHub repositories
- Searches both repository names and descriptions
- Includes repositories you own and collaborate on
- Sorts results by best match and recency
- Shows repository visibility (public/private) and descriptions
- Direct links to repository URLs

## Installation

1. Download `Github Project Search.alfredworkflow` file
2. Double-click the downloaded file to install it in Alfred
3. Configure your GitHub Personal Access Token (required)

## Setup

### 1. Create a GitHub Personal Access Token (PAT):

1. Go to [GitHub Settings → Developer Settings → Personal Access Tokens → Tokens (classic)](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Give it a descriptive name (e.g., "Alfred GitHub Search")
4. Select the `repo` scope
5. Click "Generate token"
6. Copy the generated token (you won't be able to see it again!)

### 2. Configure the Workflow:

1. Open Alfred Preferences
2. Go to the Workflows tab
3. Find the GitHub Project Search workflow
4. Click the [𝓧] button in the top-right corner
5. Add the following environment variable:
   - Name: `GITHUB_TOKEN`
   - Value: Your GitHub Personal Access Token from step 1

## Usage

1. Trigger Alfred (default: ⌘ Space)
2. Type your workflow keyword (default: `ghs`)
3. Enter your search term
4. Results will show matching repositories
5. Press Enter on a result to open the repository in your browser

## Example

```
ghs react
```
This will find all your repositories with "react" in their name or description.

## Troubleshooting

If you encounter a "404 Not Found" or "401 Unauthorized" error:
1. Check that your GitHub token is correctly set in the workflow environment variables
2. Verify that your token hasn't expired
3. Ensure your token has the `repo` scope

## License

MIT License