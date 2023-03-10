# Brainstorming

[https://gist.github.com/sharpmoose/d25487b913a08f6a6e6059c07035a041](https://gist.github.com/sharpmoose/d25487b913a08f6a6e6059c07035a041)

Liine Take Home
Python is preferred, but if you feel unable to complete it using python, use whatever programming language you feel most comfortable in.

Build an API with an endpoint that takes a single parameter, a DateTime string, and returns a list of restaurant names open on that date and time. You are provided a dataset in the form of a CSV file of restaurant names and a human-readable, string-formatted list of open hours. Store this data in whatever way you think is best. Optimized solutions are great, but correct solutions are more critical. Make sure whatever solution you come up with can account for restaurants with hours not included in the examples given in the CSV. Please include all tests you think are needed.

Assumptions:

- If a day of the week is not listed, the restaurant is closed on that day
- All times are local — don’t worry about timezone-awareness
- The CSV file will be well-formed, assume all names and hours are correct

Want bonus points? Here are a few things we would really like to see:

- A Dockerfile and the ability to run this in a container
- Using the python standard library as much as possible.
- Testing

If you have any questions, let me know. Use git to track your progress, and push your solution to a GitHub repository (public or, if private, just give me access @sharpmoose)

SOLUTION

Going to use FastAPI. We can Dockerize it: [https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi](https://fastapi.tiangolo.com/deployment/docker/#build-a-docker-image-for-fastapi)

We can easily use a Postgres Database. The challenge is to get it working with the Dockerfile we will use for the API. Looks like this link can help: [https://testdriven.io/blog/fastapi-docker-traefik/](https://testdriven.io/blog/fastapi-docker-traefik/). It looks like we will make Dockerfile for the API and then docker-compose references it from there.

API Design

datetime string param will be called time or something. Will need to parse it into the right datetime from the CSV.

Will probably do an ingest or sync route where the payload is a CSV file. Or we can embed the CSV file into the API somehow at startup. Maybe we use alembic to do it for us since alembic migrations are written in Python (This is probably the best solution).

As for accounting for the situation where no restaurant is open on a particular date/time, we should return a 404.

Database Design

Since the CSV file has datetimes as ranges, we will probably need to make multiple rows for each day with each time. This way, the database can do the heavy lifting of finding records for us.

In Python, we can get the weekday value from a given datetime like so: [https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday](https://docs.python.org/3/library/datetime.html#datetime.datetime.weekday). This will be an integer value where Monday is 0 and Sunday is 6. So we should store these weekday values as integers as well, so when we get a datetime input we can find the weekday integer value and use that as yet another filter to sqlalchemy.

We will use alembic and the migration files can be written in Python. We will need to develop some kind of algorithm to parse the CSV file to store the data in the database in a meaningful way.

We will need to parse the weekday string to determine the number of rows we will make. The open and close times will both be their own column. So we will end up with 3 filters on the query, the weekday, greater than or equal to start time and less than or equal to end time. Postgresql supports Time as a data type: [https://www.postgresql.org/docs/current/datatype-datetime.html](https://www.postgresql.org/docs/current/datatype-datetime.html)

Database Schema

1. ID
2. Restaurant Name
3. Weekday
4. Open Time
5. Close Time

Pydantic Schema

1. id
2. name
3. weekday
4. open
5. close

STATUS

Added requested route and validated manually that the number of records being imported is correct. At this point, I can add more tests. I thought about making the API return 404 when there are no restaurants open but this doesn't make a whole lot of sense to me as 404 is usually the route that doesn't exist.

END STATUS

Time Tracking

This brainstorming was from Dec 6th - 8:26pm to 9:02pm (36 minutes)

Project setup: Dec 6th - 10:23 PM to 12:02 PM (99 minutes)

CSV Import: Dec 7th - 8:18 PM to 11:22 PM (184 minutes)

Requested Route: Deb 8th - 4:32 pm to 5:35 pm (63 minutes)

More Tests: Dec 11th - 9:44 pm to 10:45 pm (61 minutes)

Total Time = 443 minutes or (7 Hours & 23 minutes)
