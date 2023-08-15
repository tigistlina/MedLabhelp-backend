# MedLab Help Backend
As every patient knows, medical jargon can be confusing for even the most routine of tests. That's why we created MedLab Help. We wanted a user-friendly guide to help you understand lab tests and give you the knowledge to allow you to be proactive in your healthcare by explaining why a test may be ordered by your doctor and what the normal range of reference for your results should be.


## Project Requirements
asgiref==3.7.2
Django==4.2.3
django-extensions==3.2.3
djangorestframework==3.14.0
gunicorn==21.2.0
packaging==23.1
psycopg2==2.9.6
pytz==2023.3
sqlparse==0.4.4
typing_extensions==4.7.1
django-cors-headers==4.2.0

## Project Setup
1. Fork this project repo to your own personal account
2. Clone this new forked project
3. Create a virtual environment by running 
    $ python3 -m venv venv
	$ source venv/bin/activate

4. Install dependencies by running $ pip install -r requirements.txt

5. Create a development database named medlab_api_development

6. Run $ python3 manage.py runserver

7. Run $ python3 manage.py makemigrations app 
       $ python3 manage.py migrate  to create the table in the database

8. Run $ python3 manage.py runscript load to import the data from the .csv into the database

9. Run $ python3 manage.py test to run tests


