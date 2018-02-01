# Boards learning project
> We have several boards that will behave like categories. 
Then, inside a specific board, a user can start a new discussion by creating a new topic.
In this topic, other users can participate in the discussion posting replies.



![](header.png)

## Installation

 * Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
 * Install [VirtualBox Oracle VM VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads)
 * Install [Vagrant](https://www.vagrantup.com/downloads.html)
 * Install Vagrant plugins:
 ```sh
 * vagrant plugin install vagrant-json-config
 * vagrant plugin install vagrant-rsync-back
 * vagrant plugin install vagrant-digitalocean
```

## Local Development Workflow

* `git clone` this repository:
```bash
# Clone with HTTPS
$ git clone https://github.com/curious725/sibt-django-guide.git
# or Clone with SSH
$ git clone git@github.com:curious725/sibt-django-guide.git
```  

* To start development run on your local machine
```bash
 $ cd sibt-django-guide
 $ vagrant up dev
  ```
  Now run inside vagrant machine:
 ```bash
 $ vagrant ssh dev
 $ cd /vagrant
 $ source venv/bin/activate
 $ cd /myproject
 $ python manage.py runserver 0.0.0.0:8000
 ```
 * Navigate to [http://localhost:8000/](http://localhost:8888/) to access server.
 
 ## Initial Deployment
 This project is using also Vagrant to simplify deployment.
 You can deploy project to DigitalOcean as we preconfigured inside Vagrantfile that
 our production will be DigitalOcean droplet.
 
 ```bash
 $ vagrant up prod --provider digital_ocean --no-provision
 $ vagrant provision prod
 ```
 
 Now e.g. you can ssh into your production machine:
  ```bash
 $ vagrant ssh prod
 ```
 
  ## Consistent Provision
 But never install programs manually on command line.
 Please instead update provision.sh script.
 After updating provision.sh script, run
 * to synchronize local environment
 ```bash
 $ vagrant provision dev
 ```
  * to synchronize production environment
 ```bash
 $ vagrant provision prod
 ```
