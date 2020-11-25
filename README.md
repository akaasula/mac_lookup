# mac_lookup

## This application takes the mac address as input, looks up in https://macaddress.io/  and provides you the vendor details like company name.

#### _For this application you need to install docker and git in you linux system_

### Usage and Requirements
#### 1. Install Docker
Use the following commands for docker installation in your linux 
`sudo apt-get update`


Next, it’s recommended to uninstall any old Docker software before proceeding.

`sudo apt-get remove docker docker-engine docker.io`

Now to install docker, enter the following command in the terminal

`sudo apt install docker.io`

The Docker service needs to be setup to run at startup. To do so, type in each command followed by enter:

`sudo systemctl start docker`
`sudo systemctl enable docker`


#### 2. Install Git
Use the following commands to install git in your linux server 

`sudo apt update`
`sudo apt install git`

To verify whether git is installed or not, use the following command
`git --version`

#### 3. Clone the files from the GitHub

Run the following commands for clonning the files from git hub.

`git clone https://github.com/akaasula/mac_lookup.git`

Then, run these commands one after the other to build the docker and run it.

`cd mac_lookup/`

`sudo docker build . -t mac_lookup`

`docker run -it mac_lookup`




##### akaasula@cisco.com




 

