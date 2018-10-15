FROM jupyterhub/jupyterhub-onbuild
RUN /opt/conda/bin/pip3 install oauthenticator jupyterhub mcpi
RUN /opt/conda/bin/conda install --yes -c conda-forge JupyterHub
RUN /opt/conda/bin/conda install --yes notebook
RUN /opt/conda/bin/npm install -g configurable-http-proxy