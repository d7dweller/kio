# kio
Content for khris.io website

## How To
In Docker Container
===================
1. Clone the repo and chage directories into the repo.

`git clone https://github.com/notkhris && cd kio`

2. Build the docker image:

`docker build -t site:latest .`

3. Run the image to generate the site content:

`sudo docker run -v /srv/site:/builder/output site:latest`

 *(`/srv/site` should be whereever you want the generated site.)*

4. Run a webserver with the generated website:

` docker run -d -v /srv/site:/usr/share/nginx/html -p 80:80 nginx:latest`


Python Virtual environment
==========================
1. Create virtual environemnt (in python36):

`python36 -m venv site`

2. Change to newly created directory and activate the virtual environment:

`cd site && source bin/activate`

3. Pull down the repo and enter the directory. (you should also pull the *crowsfoot* repo if you want to use the same theme):

`git clone https://github.com/notkhris/kio && cd kio`

   *To pull `crowsfoot` theme:* `git clone https://github.com/notkhris/crowsfoot`

4. Install the requirements:

`pip install -r requirements.txt`

5. Run generate the html & run the developent server:

`make html devserver`


