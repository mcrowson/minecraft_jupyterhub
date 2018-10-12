from oauthenticator.github import LocalGitHubOAuthenticator
import os

c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator
c.LocalGitHubOAuthenticator.create_system_users = True

c.Authenticator.whitelist = set(os.environ.get('JUPYTERHUB_ADMIN', '').split(','))
c.Authenticator.admin_users = set(os.environ.get('JUPYTERHUB_ADMIN', '').split(','))
