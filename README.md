# The Archimedeans

> The Archimedeans website, written in Django

![Website Screenshot](https://i.imgur.com/uen2EwK.png)

## Usage

First setup `venv`. You can do this with

```shell
$ python3 -m venv venv
$ . venv/bin/activate
```

Then make sure you have Python and Django installed, then you can run

```shell
$ python manage.py migrate
$ python manage.py createsuperuser # Follow the prompts
$ python manage.py runserver
```

You will also need to put the files in `static` at the root of the web server, so that they are not handled by Django

There is also a `seed.py` file which can be used to initialize the members, events and committee databases (though eventually we will migrate to doing proper backups).