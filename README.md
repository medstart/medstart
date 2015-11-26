# medstart
Please follow these steps to complete the setup:
1. git clone ssh xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
2. create v-env and activate
3. cd /src
4. git checkout develop
5. pip install -r requirement.txt (this will install all the dependencies of project)
6. create a new db and add a new file in /start/settings/<yourname_local.py> and give the DB details there , for example        refer /start/settings/base.py (Be ensure that you are not making this as gitignore)
7. give the security key accordingly to your setting file (call me up to know how to do and what is the moto behind this        local setting file)
8. Run command : python manage.py makemigrations
9. Run command : python manage.py migrate
10. Run command : python manage.py runserver 0.0.0.0:'your fav port number'
                 
                "YOU HAVE DONE WITH THE SETUP... Enjoy Coding!!" 
