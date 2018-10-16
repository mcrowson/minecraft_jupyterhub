# Minecraft with Python
This repo shows how to setup a Minecraft Server that gives users the ability to change the world through Python.
Docker all the things. This will be running a Spigot Minecraft 1.13.1 server with the RaspberryJuice Plugin that allows
Python API calls. Interaction with the Minecraft server will be done through the [mcpi](https://github.com/martinohanlon/mcpi) library with 
API instructions available [here](https://www.stuffaboutcode.com/p/minecraft-api-reference.html).

Jupyterhub                 |  Minecraft
:-------------------------:|:-------------------------:
![](https://user-images.githubusercontent.com/6452882/47052283-b2721580-d175-11e8-85f9-1aa644a11258.png)  |  ![](https://user-images.githubusercontent.com/6452882/47052284-b2721580-d175-11e8-97dc-52ae7e4110b8.png)



This project was created for the purposes of teaching introductory Python concepts.

### Setup
This will run a Minecraft server and JupyterHub behind and NGINX proxy. SSL is done via Let's Encrypt for secure access to JupyterHub. Users
auth to the JupyterHub via GitHub OAuth. 

Create a GitHub OAuth application that we will link to JupyterHub [https://github.com/settings/applications/new](https://github.com/settings/applications/new)
with https://subd.domain.com/hub/oauth_callback as the callback URL. 

Note the client_id and client_secret that GitHub provides after creation. We will need them below.

### Environment Variables
You will configure these services through environment variables. Below is a list of the variables you need to change before launching the stack. The
sections below are the services in the docker-compose.yml file.

#### jupyterhub
- OAUTH_CALLBACK_URL: This will be the callback URL you provided to GitHub when creating the application eg. https://subd.domain.com/hub/oauth_callback
- GITHUB_CLIENT_ID: The client_id GitHub provided after creationg the application.
- GITHUB_CLIENT_SECRET: The client_secret GitHub provided after creating the application
- VIRTUAL_HOST: The domain that jupyterhub will be accessed at. eg sub.domain.com
- LETSENCRYPT_HOST: The domain that jupyterhub will be accessed at. eg sub.domain.com
- LETSENCRYPT_EMAIL: The contact email for Let's Encrypt eg. admin@domain.com
- JUPYTERHUB_ADMIN: The GitHub username for the first Admin account; supply multieple names separated by commas. Subsequent users can be added through the JupyterHub GUI after launch.

### Launch
`docker-compose up -d`

To give your minecraft user Operator privleage, open up RCON cli.
```bash
docker-compose exec minecraft rcon-cli
> op MINECRAFTNAME
```

Open your Minecraft Java client and connect to your Multiplayer Server, once you're in game,
open up a Jupyter notebook at your domain, and try the following.

```python
from mcpi import minecraft
mc = minecraft.Minecraft.create('minecraft')
mc.postToChat("Hello Minecraft World")
```
If you see your message in the chat, all is working!


### Additional Resources
I found the following very helpful in setting this up:
 - [CoderDojo Docs](https://coderdojotc.readthedocs.io/projects/python-minecraft/en/latest)
 - [JupyterHub Setup Talk](https://www.youtube.com/watch?v=gSVvxOchT8Y)
