https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-uwsgi-and-nginx-on-ubuntu-16-04

-above link use two sites by name firstsite and secondsite. I use ony one site by name my_app.

-Env file and codes in git that in bellow instruction clone from git hub



run bellow command by root user :

pip install virtualenv virtualenvwrapper
echo "export WORKON_HOME=~/Env" >> ~/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc
cd 
git clone https://github.com/universcom/simple_django_web_app.git
apt-get install python-dev
pip install uwsgi     ------> this command take a minutes
mkdir -p /etc/uwsgi/sites
cp my_app.ini /etc/uwsgi/sites/ -pvr 
cp uwsgi.service /etc/systemd/system/
apt-get install nginx
rm /etc/nginx/sites-enabled/default
cp nginx.conf /etc/nginx/sites-available/my-app
ln -s /etc/nginx/sites-available/my-app /etc/nginx/sites-enabled
nginx -t
systemctl restart nginx
systemctl start uwsgi
systemctl enable nginx
systemctl enable uwsgi

- change configs file based on your enviroment.
