# NEIGHBOURHOOD
#### By Charles Okunzo, June 21, 2022
### This application helps individuals from a given area to connect through a community.


## Table of Contents
+ [Description](#description)
+ [Installation Requirements](#installation)
+ [Technologies Used](#technology)
+ [Lisence](#lisence)
+ [Authors Info](#author)

## Description
This application helps individuals from a given area to connect through a community.
    As a user I would like to:

- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.
...
```
Landing Page
```
<img src="static/images/Screenshot from 2022-06-20 00-10-58.png">

```
Sign Up
```

<img src="static/images/Screenshot from 2022-06-20 00-11-11.png">

```
Log In
```

<img src="static/images/Screenshot from 2022-06-20 00-11-16.png">

```
Dashboard
```

<img src="static/images/Screenshot from 2022-06-20 00-14-08.png">


[Go Back to the top](#neighbourhood)

## Getting Started

To clone the repository, run:

    git clone https://github.com/charles-okunzo/neighbourhood

Then navigating to the cloned directory:

    cd neighbourhood


### Prerequisite
This project requires a prerequisite understanding of the following:
- Django Framework
- Python3.8
- Postgres
- Python pipenv
- Makefile


## Setup and installation

###  Activate virtual environment
Activate virtual environment using python3.8 as default handler
    `pipenv shell`
####  Install dependancies
Install dependancies that will create an environment for the app to run from `Pipfile`
####  Create the Database
    - psql
    - CREATE DATABASE neighbourhood;
####  .env file
Create .env file and paste the following, filling where appropriate:

    SECRET_KEY = '<secret_key>'
    DB_NAME = '<db_name>'
    DB_USER = '<username>'
    DB_PASSWORD = '<password>'

#### Run initial Migration
    make migrate
    
#### Run the app
    make run or make
    
    Open terminal on localhost:

[Go Back to the top](#neighbourhood)
    
## Deployment

The application is deployed on Heroku and is live on this link:

[https://my-h00d.herokuapp.com/](https://my-h00d.herokuapp.com/)

## Technologies Used

  - [Django 4.0.5](https://docs.djangoproject.com/en/4.0/releases/4.0.4/) - Backend logic of the application and views.
  - [Bootstrap](https://getbootstrap.com/) - Used for overall design and responsive site


## Known Bugs
No known bugs.


## Licence

copyright (c) 2022 MIT License. [View License Here](LICENSE)

[Go Back to the top](#neighbourhood)

## Authors Info

* Slack Profile - [Charles Okunzo](https://app.slack.com/client/T0101L740P4/C010GLANY3A/user_profile/U02TTFQ0VJR)
* Email address - [Charles Okunzo](charles.okunzo@student.moringaschool.com)