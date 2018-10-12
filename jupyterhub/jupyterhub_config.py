from oauthenticator.github import LocalGitHubOAuthenticator
import os

c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.JupyterHub.port = 443

c.Authenticator.whitelist = set(os.environ.get('JUPYTERHUB_ADMIN'),)
c.Authenticator.admin_users = set(os.environ.get('JUPYTERHUB_ADMIN'),)
