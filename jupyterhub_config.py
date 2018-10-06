from oauthenticator.github import LocalGitHubOAuthenticator

c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator
c.LocalGitHubOAuthenticator.create_system_users = True

c.JupyterHub.port = 443
c.JupyterHub.ssl_key = "/etc/letsencrypt/privkey.pem"
c.JupyterHub.ssl_cert = "/etc/letsencrypt/cert.pem"

with open('/srv/jupyterhub/hub_users.txt') as f:
    user_names = [l.strip() for l in f.readlines()]
with open('/srv/jupyterhub/hub_admin.txt') as f:
    admin_names = [l.strip() for l in f.readlines()]
c.Authenticator.whitelist = set(user_names)
c.Authenticator.admin_users = set(admin_names)
