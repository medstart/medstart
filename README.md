# medstart
Please follow these steps to complete the setup:<br>
1. git clone ssh xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx<br>
2. create v-env and activate<br>
3. cd /src<br>
4. git checkout develop and take latest pull <br>
5. pip install -r requirement.txt (this will install all the dependencies of project)<br>
6. create a new db and add a new file in /start/settings/<yourname_local.py> and give the DB details there , for example<br>        refer /start/settings/base.py (Be ensure that you are not making this as gitignore)<br>
7. give the security key accordingly to your setting file (call me up to know how to do and what is the moto behind this        local setting file)<br>
8. Run command : python manage.py makemigrations<br>
9. Run command : python manage.py migrate<br>
10. Run command : python manage.py runserver 0.0.0.0:'your fav port number'<br>
                 
                "YOU HAVE DONE WITH THE SETUP... Enjoy Coding!!" 
