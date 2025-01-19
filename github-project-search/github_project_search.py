import sys
import requests
import json
import os

# GitHub configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_API_URL = 'https://api.github.com'

def search_repos(query):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    try:
        # Get all repositories for the authenticated user
        repos_response = requests.get(
            f'{GITHUB_API_URL}/user/repos',
            headers=headers,
            params={
                'per_page': 100,
                'sort': 'updated',
                'direction': 'desc',
                'affiliation': 'owner,collaborator'  # Include repos you own and collaborate on
            }
        )

        if repos_response.status_code != 200:
            return [{
                'title': f'Error fetching repositories: {repos_response.status_code}',
                'subtitle': repos_response.json().get('message', 'Unknown error'),
                'valid': False
            }]

        repos = repos_response.json()

        # Filter repositories based on search query
        query_lower = query.lower()
        filtered_repos = [
            repo for repo in repos
            if query_lower in repo['name'].lower() or
               query_lower in (repo.get('description', '') or '').lower()
        ]

        if not filtered_repos:
            return [{
                'title': f'No matching repositories found',
                'subtitle': f'Try a different search term | Total repos available: {len(repos)}',
                'valid': False
            }]

        # Sort results by best match and recency
        results = []
        for repo in filtered_repos:
            # Calculate match quality (name match is better than description match)
            name_match = query_lower in repo['name'].lower()
            match_quality = 2 if name_match else 1

            results.append({
                'title': repo['name'],
                'subtitle': f"{':lock: ' if repo['private'] else ''}[{repo.get('visibility', 'unknown')}] {repo.get('description', '')}",
                'arg': repo['html_url'],
                'match_quality': match_quality,
                'updated_at': repo.get('updated_at', ''),
                'icon': {
                    'path': 'icon.png'  # You can add a custom icon for your workflow
                }
            })

        # Sort by match quality (exact matches first) and then by update date
        results.sort(key=lambda x: (-x['match_quality'], x['updated_at']), reverse=True)

        # Remove the sorting metadata before returning
        for result in results:
            del result['match_quality']
            del result['updated_at']

        return results

    except requests.exceptions.RequestException as e:
        return [{
            'title': 'Error occurred',
            'subtitle': f'Error: {str(e)}',
            'valid': False
        }]

if __name__ == "__main__":
    if not GITHUB_TOKEN:
        print(json.dumps({
            'items': [{
                'title': 'Error: GitHub token not found',
                'subtitle': 'Please check your GitHub PAT in Alfred workflow environment variables',
                'valid': False
            }]
        }))
        sys.exit(1)

    query = sys.argv[1] if len(sys.argv) > 1 else ''
    results = search_repos(query)
    print(json.dumps({'items': results}))