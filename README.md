# The Archimedeans

> The Archimedeans website, written in Django

![Website Screenshot](https://i.imgur.com/uen2EwK.png)

## Usage

Make sure you have Python and Django installed, then you can run

```shell
$ python manage.py migrate
$ python manage.py createsuperuser # Follow the prompts
$ python manage.py runserver
```

You will also need to put the files in `static` at the root of the web server, so that they are not handled by Django

## Notes

Currently the rest of the website is not implemented, just the member management system (and only from the Django admin panel, at the moment).