# Invest blog

![App image](https://i.ibb.co/DbGgxp6/image.png)

App represents a pet-project for studying Django. 

It has 7 models: Mentor, Student, Category, Course, Lesson, Schedule and Tag. Every
course has its own category and responsible. Every lesson has its own course, mentor and tags.
Every schedule has its own lesson, student and lesson time.

It's possible to browse all courses, all mentors and every instance of those models in detail.
Staff member has a possibility to add, update and delete courses.

All views have been optimized in terms of queries to db with help of django-debug-toolbar. 

It was added tests and fake data creation.

It was added contact form for sending messages via task queue. When the message is sent, 
administrator receives this message and sender receives a notification.

## Install

Python3 and Git should be already installed. 

1. Clone the repository by command:
```console
git clone https://github.com/balancy/invest-blog
```

2. Go inside cloned repository and create virtual environment by command:
```console
python -m venv env
```

3. Activate virtual environment. For Linux-based OS:
```console
source env/bin/activate
```
&nbsp;&nbsp;&nbsp;
For Windows:
```console
env\scripts\activate
```

4. Install requirements by command:
```console
pip install -r requirements.txt
```

5. Rename `.env.example` to `.env` and define your propre values for environmental variables:

- `DEBUG` — debug mode
- `SECRET_KEY` — project django secret key
- `ALLOWED_HOSTS` — see [Django documentation](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- `EMAIL_HOST` = project email host (for sending emails)
- `EMAIL_PORT` = project email port
- `EMAIL_HOST_USER` = project admin email
- `EMAIL_HOST_PASSWORD` = project admin email password
- `EMAIL_USE_SSL` = does project use SSL?

## Launch

1. Make migrations
```console
python3 manage.py migrate
```

2. Create superuser
```console
python manage.py createsuperuser 

```
3. Run server
```console
python manage.py runserver
```

## In case you need to send emails 

1. Launch redis server and queue workers

They don't work in Windows, so if you have one, you need to launch them in 
   emulated unix-OS (wsl-subsystem)

Launch server in one terminal
```console
redis-server
```

2. Launch workers in another terminal
```console
celery -A invest_blog worker -l INFO
```