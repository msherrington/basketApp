# BasketApp

Single Page Application built with Django and AngularJS

## Command Line Setup

### BACKEND

1. Install Python3

    ###### (This app was created with Python 3.6.6)
    [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone the repository

    [https://github.com/msherrington/basketApp](https://github.com/msherrington/basketApp)

3. Navigate to the backend directory

    `/basketApp/backend`

4. Create a virtual environment

   `python3 -m venv venv`

5. Activate virtual environment

   `source venv/bin/activate`

6. Upgrade/Install PIP Package Manager

    It should have been installed with Python, so just follow the upgrade instructions on this link...

    [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/)

    Otherwise see installation instructions on the same page


7. Install project requirements within the virtual environment

   `pip install -r backend/basket/requirements.txt`

8. Create all database migrations

    `./manage.py makemigrations`<br/>
    `./manage.py makemigrations items`<br/>
    `./manage.py makemigrations orders`<br/>
    `./manage.py makemigrations orderitems`

9. Apply model changes to DB schema

    `./manage.py migrate`

10. Run the backend server

    `./manage.py runserver`

#

### FRONTEND


1. Install NodeJS and npm (Node Package Manager)

    [https://docs.npmjs.com/downloading-and-installing-node-js-and-npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

2. Navigate to the frontend directory

    `/basketApp/frontend`

3. Install Bower

    `npm install bower`

4. Install project requirements

    `npm i`<br/>
    `bower i`

4. Run the frontend server

    `grunt serve`

5. Open the basketApp

    Open a browser window and navigate to [localhost:9000/index.html](localhost:9000/index.html)

