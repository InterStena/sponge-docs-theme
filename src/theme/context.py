import os


def _split_environment_variable(name):
    value = os.environ.get(name)
    return value and value.split()


def _load_downloads():
    # Path to a downloadable ZIP with the HTML files
    html_download = os.environ.get('HTML_DOWNLOAD')
    return html_download and [('HTML', html_download)]


def setup_html_context():
    github_user = os.environ.get('GITHUB_USER')
    github_repo = os.environ.get('GITHUB_REPO')
    github_version = os.environ.get('GITHUB_VERSION')

    return {
        # Path to docs source directory in the repository
        'conf_py_path': '/source/',

        # List of supported languages
        'locales': _split_environment_variable('LOCALES'),

        # Current version and list of documented versions
        'current_version': os.environ.get('VERSION'),
        'versions': _split_environment_variable('VERSIONS'),

        # List of available downloads (for offline usage)
        'downloads': _load_downloads(),

        # Link to GitHub repository
        'display_github': github_user and github_repo and github_version,
        'github_user': github_user,
        'github_repo': github_repo,
        'github_version': github_version,
    }
