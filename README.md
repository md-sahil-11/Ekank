# Ekank
###### It is an emulation of Employees leave management system.

## Technology Stack:
### Backend
* #### Django(Python3)

### Database
* #### SQLite
  ###### This is only used for development purpose and a more powerful datatbase should be used in production.

## How to Use?
* Create a python3 virtual environment, navigate to project directory on terminal and install dependencies(listed in requirements.txt file) using the command
`pip install requirements.txt` <br>
RUN `python manage.py makemigrations` and `python manage.py migrate` <br>to create tables in database. <br>
To run server, use command `python manage.py runserver`

* Open a browser and navigate to <b>localhost:8000/leave/</b>
* Use tool like Postman to test APIs.
* In Headers include <br>
  Authorization: Token <generated_token> <br>
  Content-Type: application/json
* For generating token hit POST request to <b>http://127.0.0.1:8000/api-token-auth/</b>
* APIs for Employees <br>
  POST request for creating leave request 
      `Data body should be like {'text': <request text>}` <br>
  GET for list down of leave requests created by the employee <br>
  GET for retrieving a request
* APIs for Admins <br>
  PUT request for modifiying the status of the request which has choices of ('Accepted', 'Rejected', 'Pending') <br>
      `Data body should be like {'status': <any status>, 'employee': <id of the employee related to request>}` <br>
  GET for list down of leave requests created by all employees <br>
  GET for retrieving a request <br>
  DELETE for deleting a request
  
