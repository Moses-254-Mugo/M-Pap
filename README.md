# M-Pap


## Contributor
* Mugo Moses
* Nick Otieno
* Teresia King'ori


## Description
M-Pap is a web application that provides a real-time conversation with people and also extends one-way messaging to accept two-way communication. 


## Setup and Installation
### Requirements
1. Clone the repository by running

        https://github.com/Moses-254-Mugo/M-Pap
    Navigate to the project

        cd M-pap
 2. Create a virtual enviroment

         pip install virtualenv 

    To activate the created virtual environment, run

        source virtual/bin/activate
3. Create database
    You will need to create a new postgress database by typing the following command to access postgress

        $ psql

    Then run below query to create a new database named 

        # create databases chats ;
5. Create Database migrations
    make migrations on postgres using django

        python3.8 manage.py makemigrations chats
    then run the below command.

        python3.8 manage.py migrate

6. Run the app
    To run the application on your development machine,

        pythong3.8 manage.py runserver
### Running Tests
To run tests;

        python3.8 manage.py test


## Technologies Used
* Python3.8
* Django
* HTML
* Bootstrap
* CSS

## User Stories
1. Allows user to login
2. Allows user to create a room 
3. Allows user to chat with anyone in the room 


## License
The project is under[MIT License](LICENSE).