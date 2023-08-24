# Voxy - Word Count
Armando M. Baratti - ambarjobs@gmail.com (2023-08-24)

## Running the project

### Install Python:

You can find information on how get and install Python here:
https://wiki.python.org/moin/BeginnersGuide/Download

### Configure a Python's virtual environment

There are many ways to do this.
Here are instructions about to use one of these ways:
https://docs.python.org/3/library/venv.html

Here we'll use a virtual environment called `voxy_word_count`.

### Clone the project:

```bash
git clone https://github.com/ambarjobs/voxy_word_count.git
```
### Install dependencies:

Inside the virtual environment run:

```bash
pip install -r requirements.txt
```

### Run the web server

For running the local web server use the command in the root dir of the project:

```bash
./manage.py runserver
```

Then point your browser to `http://127.0.0.1:8000/` to get access to the web page.


## Additional information

For management commands, run `manage.py` without arguments.

```bash
./manage.py
```


## Assumptions

This is a coding challenge and so to maintain it simple and as directed by the challenge
instructions some assumptions will be taken.

Here are the assumptions made as well as some suggestions to further improvement:

### Versions of the language and framework

As the versions of Python and the choosen framework (Django) where not pre defined it was choosen
the actual last version of both (the compatibility is garanteed here:
https://docs.djangoproject.com/en/4.2/faq/install/#faq-python-version-support).

- Python: 3.11.3
- Django: 4.2.4

### Local web server

In order to keep things simple it'll be using just the simple web server provided by Django (in
fact a web server provided by Python).

In a production environment we'll need to use a WSGI server (like `uWSGI` or `gunicorn`) and a
real web server, like `nginx`.

### HTTP instead of HTTPS

Of course in production it'd be mandatory to use a certificate and configure the web server with
encription through `SSL` (HTTPS).

### Database

As the challenge don't need a database to operate (but Django does) we'll be using a `Sqlite` database
for witch we already have native access in Python and it's the default Django database when another
isn't specified.

As this is a small file and will be used only to Dajango administrative tasks it was includes on
the code base.

### Restriction to run only locally

As SSL (HTTPS) is not being used, the access is restricted to only locally (`settings.ALLOW_HOSTS`),
even whith `settings.DEBUG = False`.

### Style conventions

The code must be mainly adherent to PEP8's more strict specifications.
As the maximum line lenght is only a recomendation, it was choose 100 characters as this limit.

### New Python packages

The new `pyproject.toml` could be used for system requirements intead of `requirements.txt` file.
