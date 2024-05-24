# Practical

Set up a Ubuntu 22.04 VM

## Transfer file

Can also drag and drop or download onto VM directly

### scp (not recommended unless you want to learn something new)

```bash
# install openssh server for scp (and ssh)
sudo apt install openssh-server
# transfer file
# !!! change machine IP in command below !!!
scp mysite.zip student@CHANGE_TO_MACHINE_IP:/home/student
```

## Setup after tranfering file

```bash
# unzip zip (or can just use the gui to extract)
unzip mysite.zip

# install supervisor to startup django app automatically
sudo apt install supervisor
# install python virtualenv
sudo apt install python3-venv
# install nginx as a web server
sudo apt install nginx

# create virtualenv
python3 -m venv /home/student/mysite/venv
# activate virtualenv
source /home/student/mysite/venv/bin/activate
# install dependencies
pip install Django gunicorn

# add gunicorn config
sudo cp /home/student/gunicorn.conf /etc/supervisor/conf.d/
sudo mkdir /var/log/gunicorn
# start gunicorn with supervisor
sudo supervisorctl update

# add nginx config
# !!! change machine IP in /home/student/mysite.nginx !!!
# CHANGE_TO_MACHINE_IP
sudo cp /home/student/mysite.nginx /etc/nginx/sites-enabled/mysite
# start nginx
sudo nginx -s reload
```

## Using the site

Access http://CHANGE_TO_MACHINE_IP/ from your browser in your Kali machine.

## Restoring DB from clean slate

Make a HTTP request (doesn't matter if GET, POST) to http://CHANGE_TO_MACHINE_IP/reset to restore the database.

## Assessment objectives

Students will learn how to set up their own vulnerable lab environments, to practice web app pentesting in a safe manner.

Students will learn about the technical details of XSS, how to test and exploit such vulnerabilities to a maximum effect, as well as possible mitigation measures.

## Module Learning Objectives Supported

1. Understand the web application penetration testing methodology
2. Assess if various attack vectors exists that could be used against a web application
3. Exploit the discovered web application vulnerabilities to better understand the risks and to find other flaws

## Description

Students are to set up a vulnerable lab environment on an ubuntu virtual machine consisting of a web application vulnerable to XSS. Students will have to complete a series of tasks to learn about XSS attacks, and develop an exploit for it.
