# Minecraft with Python
This repo shows how to setup a Minecraft Server that gives users the ability to change the world through Python.
Docker all the things.

I am hosting this on a t3.small on AWS for 25 students.

### Prepare
Create a few folders that will hold mapped data to our docker containers
```bash
mkdir certs
mkdir mc_data
mkdir jupyhub_data
```
### JupyterHub
Python will be entered through Jupyter notebooks on the same server that is running the Minecraft server. We will
run JupyterHub so that each student gets their own Notebook space, and students will authenticate with their GitHub accounts.

Create a GitHub OAuth application that we will link to JupyterHub [https://github.com/settings/applications/new](https://github.com/settings/applications/new)

Then replace the values in `docker-compose.yml` of subd.domain.com with your real domain name and the values
in the GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET with the real values given at the end of the application creation process
you started above.

Enter the GitHub usernames of admin into the `hub_admin.txt` file with each name being a new line. Then enter the GitHub usernames
of all users (including admin) into the `hub_users.txt` file with each name being a new line. This only allows those listed usernames to
create notebooks.

Additional users can be added from the Jupyter Admin GUI.

Interaction with the Minecraft server will be done through the [mcpi](https://github.com/martinohanlon/mcpi) library.

##### Certificates
It is best practice for JupyterHub to be behind SSL. This can be done easily with [LetsEncrypt](https://letsencrypt.org/).

To get a temporary certificate (expires in 30 days) you could run the following:
```bash
docker run -p 80:80 -v "$(PWD)/certs:/var/www/certs" --name le -e DOMAINS='subd.domain.com' -e EMAIL='me@domain.com' dockette/letsencrypt
```

Then update the mapping in the `docker-compose.yml` to reference your real domain.

### Minecraft
This will be running a Spigot Minecraft 1.13.1 server with the RaspberryJuice Plugin.

We also whitelist for the Minecraft server. This is a bit more complex as it requires knowing the UUID of the player. These can be
looked up on websites like [https://mcuuid.net](https://mcuuid.net). Once you know these you can update the
`mc_admin.json` and `mc_users.json` files with the appropriate Minecraft usernames.

Once the server is live, you can add additional Minecraft users via `/whitelist add <playername>` command

The project is mainly driven by Docker. First make some directories for mounting the data, and then launch
the services.

Now start the services and you should have both JupyterHub and Minecraft Server running
`docker-compose up -d`

Open your Minecraft Java client and connect to your Multiplayer Server, once you're in game,
open up a Jupyter notebook at your domain, and try the following.

```python
from mcpi import minecraft
mc = minecraft.Minecraft.create('minecraft-server')
mc.postToChat("Hello Minecraft World")
```
If you see your message in the chat, all is working!

### Troubleshooting
Check docker logs if stuff is launching but doesn't seem to be working correctly

### Additional Resources
I found the following very helpful in setting this up:
 - [CoderDojo Docs](https://coderdojotc.readthedocs.io/projects/python-minecraft/en/latest)
 - [JupyterHub Setup Talk](https://www.youtube.com/watch?v=gSVvxOchT8Y)
