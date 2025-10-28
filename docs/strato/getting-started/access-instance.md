All Strato instances are run on the AAU-network. Before you attempt to access your instance, please make sure that you are connected to the AAU-network - either by being physically on university grounds, being connected to the [**AAU VPN-service**](https://www.en.its.aau.dk/instructions/vpn) or establishing the connection through the [**SSH-gateway**](/strato/getting-started/access-instance/#connecting-via-aaus-ssh-gateway/). 

Strato requires your key file to be in the OpenSSH-format, and if you have managed to create the key pair [*according to the previous section*](/strato/getting-started/launch-instance/#create-ssh-key-pair), it's safe to assume that you have OpenSSH installed on your machine. 

The following will work on most modern computers, but for Windows users we specifically recomend using either Powershell (comes preinstalled on all Windows computers), [MobaXterm](https://mobaxterm.mobatek.net/) or [PuTTY](link). Do not rely on the console built in the OpenStack dashboard.

## Access your instance

Open the appropriate terminal application for your system and enter the SSH command. 

The command structure is:

```
ssh -i ~/.ssh/<my_private_key> ubuntu@10.92.0.zzz
```

* `ssh` is a call for establishing an SSH-connection. 
*  `-i` is an additional argument for specifying an identity file (private key).
* `~/.ssh/yourPersonalKey` is the typical location of your private key (identity file). Don't forget to swap this out for the actual location of your SSH-key.
* `ubuntu@10.92.10.zzz` specifies which user you want to log in as, and the IP adress of the instance you want to connect to (can be found in the OpenStack dashboard; *Compute > Instances *)

The command should look something like this:

```
ssh -i ~/.ssh/my_ssh_key ubuntu@10.92.1.99
```

<p style="font-weight: bold; font-size: 19px;">You should now have accessed your instance!</p> 

### Additional information

**Usernames for other distribution images**

The default user name for Ubuntu-instances is always *"ubuntu"*. If you decide to try out a different distribution image, this would change. 

**Connecting via AAU's SSH-gateway**

If you do not have access to the VPN, it is also possible to connect to your instance by using AAU's SSH gateway as a jump host. This way your connection gets established through the gateway without redirecting the rest of your network traffic. Note that this will ask you for [multifactor authentication](https://www.en.its.aau.dk/instructions/mfa). 

```
ssh -J <aau_username>@sshgw.aau.dk -i  ~/.ssh/my_ssh_key ubuntu@10.92.1.99
```
Where you switch out *<aau_username>* for your actual username, like so:
```
ssh -J kf41yf@dep.aau.dk@sshgw.aau.dk -i  ~/.ssh/my_ssh_key ubuntu@10.92.1.99
```

**File permissions**

It is possible, you might be faced with an error message telling you *"Permissions are too open"*. In order to solve this you need to modify the file permissions:
```
chmod 600 ~/.ssh/my_ssh_key
```
![Placeholder](/assets/img/openstack/ssh_instance.gif){ loading=lazy }



