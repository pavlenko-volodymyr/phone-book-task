A Mayor of a small town decided to digitize internal phone book.
You agreed on writing simple REST API server as the first step.
The task is very urgent and the customer expects to receive code within next 3 hours 
from the receipt of the assignment.

Requirements
------------
The REST api server must be written in `python` using `flask` framework.
The server must accept and return data in JSON format.
As a database it may use either SQLite or PostgreSQL.
There must be a `/directory` resource representing a phone book and it's possible to:
- Add new items
- Modify existing items
- Delete existing items
It should support query argument: `district` to filter response by name of the district in which a person lives.
Items is consisting of the following fields:
- `First name`
- `Last name`
- `Phone number`
- `Address`

Bonus
-----
The application should be wrapped up in Docker container(s).
