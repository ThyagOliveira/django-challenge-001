# Jungle Devs - Django Challenge #001

## Description

**Challenge goal**: The purpose of this challenge is to give an overall understanding of a backend application. You’ll be implementing a simplified version of a news provider API. The concepts that you’re going to apply are:

- REST architecture;
- Authentication and permissions;
- Data modeling and migrations;
- PostgreSQL database;
- Query optimization;
- Serialization;
- Production builds (using Docker).

**Target level**: This is an all around challenge that cover both juniors and experience devs based on the depth of how the concepts were applied.

**Final accomplishment**: By the end of this challenge you’ll have a production ready API.

## Acceptance criteria

- Clear instructions on how to run the application in development mode
- Clear instructions on how to run the application in a Docker container for production
- A good API documentation or collection
- Login API: `/api/login/`
- Sign-up API: `/api/sign-up/`
- Administrator restricted APIs:
  - CRUD `/api/admin/authors/`
  - CRUD `/api/admin/articles/`
- List article endpoint `/api/articles/?category=:slug` with the following response:
```json
[
  {
    "id": "39df53da-542a-3518-9c19-3568e21644fe",
    "author": {
      "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
      "name": "Author Name",
      "picture": "https://picture.url"
    },
    "category": "Category",
    "title": "Article title",
    "summary": "This is a summary of the article"
  },
  ...
]
```
- Article detail endpoint `/api/articles/:id/` with different responses for anonymous and logged users:

    **Anonymous**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>"
    }
    ```

    **Logged user**
    ```json
    {
      "id": "39df53da-542a-3518-9c19-3568e21644fe",
      "author": {
        "id": "2d460e48-a4fa-370b-a2d0-79f2f601988c",
        "name": "Author Name",
        "picture": "https://picture.url"
      },
      "category": "Category",
      "title": "Article title",
      "summary": "This is a summary of the article",
      "firstParagraph": "<p>This is the first paragraph of this article</p>",
      "body": "<div><p>Second paragraph</p><p>Third paragraph</p></div>"
    }
    ```

## Instructions

##### Configure virtualenv
```shell
$ python -m venv venv
$ source venv/bin/activate
$ (venv) pip install -r requirements.txt
```

##### Environment Variables
Rename `.env.example` to `.env` and configure:
- [DATABASE_URL](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DATABASES)
- [DEBUG](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-DEBUG)
- [SECRET_KEY](https://docs.djangoproject.com/en/3.1/ref/settings/#std:setting-SECRET_KEY).

Generate Secret Key
```shell
$ python
$ import secrets;secrets.token_urlsafe(20)
```

Install [Docker](https://docs.docker.com/get-docker/)
##### Create base volume
```shell
$ docker volume create base-volume
```
##### Start container
```shell
$ docker-compose -f docker-compose-dev.yml up
```
##### Container access
```shell
$ docker-compose -f docker-compose-dev.yml exec app bash
```
##### Create super user
```shell
$ python manage.py createsuperuser
```

## API Documentation

##### Swagger
- Access `http://localhost:8000/api/docs`
- Authentication
  - Use endpoint `auth/login` to get the token
  - Put the token in `Authorize` as follows: `Bearer token-here`
  