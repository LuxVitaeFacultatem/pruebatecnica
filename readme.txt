1. Running the the code localy: 

- create an environment in Python, you can make use of virtual environments. A virtual environment allows you to have isolated Python environments with their own installed packages, which can help you manage dependencies and avoid conflicts between different projects. Here's how you can create a Python environment using the venv module:

Explanation: 

a) Open a command prompt or terminal window.

b) Create a new directory for your environment (optional, but recommended): mkdir myenv

c) Change to the newly created directory: cd myenv

d) Create a virtual environment using the venv module: python -m venv env
   Here, env is the name of the virtual environment. You can choose any name you like.

e) Activate the virtual environment:
   For Windows: env\Scripts\activate
   For macOS/Linux: source env/bin/activate

Once activated, your command prompt or terminal should show the virtual environment's name in parentheses, indicating that you're working within the environment.

f) Now you can install packages and work with your Python environment.

Remember to activate the virtual environment every time you want to work on your project. This ensures that you're using the correct Python interpreter and packages installed within that environment.

If you want to deactivate the virtual environment and return to your system's global Python environment, simply use the following command:

For Windows: deactivate
For macOS/Linux: deactivate

-------------

Install an requeriments.txt file:

To install the packages listed in a requirements.txt file, you can use the pip package manager in Python. Here's how you can do it:

a) Make sure you have pip installed on your system. If you don't have it, you can install it by following the instructions at https://pip.pypa.io/en/stable/installing/.

b) Open a command prompt or terminal window.

c) Navigate to the directory where your requirements.txt file is located.

d) Activate your virtual environment (if you're using one) by following the activation steps mentioned in the previous response.

e) Install the requirements using pip with the -r flag, specifying the path to your requirements.txt file: 

pip install -r requirements.txt

This command will read the requirements.txt file and install all the packages listed within it.

f) Wait for pip to download and install the packages. Once the process is complete, all the packages and their dependencies will be installed in your Python environment.

That's it! The packages specified in the requirements.txt file should now be installed and ready for use in your Python environment.

-------------

Import an bd in PostgreSQL:

a) Launch pgAdmin 4 and connect to your PostgreSQL server.

b) Right-click on the "Databases" node in the Object Browser and select "Create" and then "Database...".

c) In the "Create - Database" dialog, enter the name of the new database and click "Save" to create it.

d) Right-click on the newly created database and select "Restore...".

e) In the "Restore" dialog, go to the "Filename" tab.

f) Click on the folder icon next to the "Filename" field to browse for the backup file.

g) Locate and select the backup file (usually a .sql file or a compressed .tar or .zip file) and click "Open".

h) In the "Restore" dialog, make sure the "Format" is set correctly based on the format of your backup file (e.g., "Custom" for a .tar file or "Plain" for a .sql file).

i) Optionally, you can select additional options such as "Clean before restore" to drop existing objects before restoring, or "Only data" to restore only the data without the schema.

j) Click the "Restore" button to start the restoration process.

k) Wait for the restore process to complete. You'll see a progress bar indicating the status of the restore operation.

m) Once the restore is finished, you should see a success message indicating that the restore operation completed successfully.



The database should now be imported into your PostgreSQL server using pgAdmin

You can explore the restored database and start working with its tables, views, and other objects.

-------------

Run the flask python .\src\app.py:

a) Open a command prompt or terminal window.

b) Navigate to the directory where your Flask application is located. You can use the cd command to change directories. For example, if your Flask application is located in the src directory:  cd path/to/src

c) Activate your virtual environment (if you're using one) by following the activation steps mentioned earlier.

d) Run the Flask application by executing the following command:  python app.py

e) Flask will start the development server, and you should see some output indicating that the server is running. By default, the Flask development server runs on http://127.0.0.1:5000/.

f) Open a web browser and visit http://127.0.0.1:5000/ to see your Flask application in action.

---------------------------------------------------------------------------------

2. Run Flask tests using the unittest:

a) Create a test file: Create a new Python file in your project directory, for example, test_flask_app.py, where you'll write your Flask tests.

b) Import the necessary modules: At the beginning of your test file, import the required modules:

   import unittest
   from flask import Flask, jsonify
   from your_application_file import app

c) Define a test class: Create a subclass of unittest.TestCase and define your test methods within it:

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Optional: Perform any setup tasks here before each test

    def tearDown(self):
        # Optional: Perform any teardown tasks here after each test

    def test_route(self):
        # Write your test logic here
        # Make requests to the Flask app and assert the expected responses
        pass

    def test_another_route(self):
        # Write another test here
        pass


d) Implement test methods: Inside each test method, you can use Flask's test client to make requests to your Flask application and assert the expected responses. Here's an example of testing a route that expects a JSON response:

    def test_route(self):
        with app.test_client() as client:
            response = client.get('/your_route')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')
            # Add more assertions based on the expected response

e) Run the tests: To run the tests, you can use the unittest module's test runner. You can do this by adding the following code at the end of your test file:

if __name__ == '__main__':
    unittest.main()


f) Execute the tests: Open a command prompt or terminal window, navigate to your project directory, and run the test file using the Python interpreter:

python test_flask_app.py


g) The tests will be executed, and you will see the test results in the console.

---------------------------------------------------------------------------------

3. Deploy a Flask REST API on Heroku:

a) Create a Heroku account: If you don't have one already, sign up for a free account at Heroku's website (https://www.heroku.com/) and log in.

b) Install the Heroku CLI: Download and install the Heroku Command Line Interface (CLI) appropriate for your operating system by following the instructions at https://devcenter.heroku.com/articles/heroku-cli.

c) Set up your Flask app:

   Create a new directory for your Flask app.
   Inside the directory, create a virtual environment and activate it.
   Install Flask and any other necessary dependencies.
   Create a requirements.txt file in the project root to specify your dependencies.

d) Initialize a Git repository: Run the following commands in your project directory:

git init
git add .
git commit -m "Initial commit"

e) Log in to Heroku CLI: Open a command prompt or terminal and run: heroku login

f) Create a new Heroku app: Run the following command, replacing your-app-name with your desired app name (must be unique):
heroku create your-app-name

g) Configure Heroku to use Git: Run the following command:
heroku git:remote -a your-app-name

h) Deploy your app to Heroku: Run the following command to push your code to the Heroku remote repository:

git push heroku master

i) Scale your app: By default, Heroku runs a single web dyno. Scale it to ensure your app is up and running:
heroku ps:scale web=1

j) Visit your app: After the deployment is complete, you can open your app in a browser using the following command: heroku open

k) Test your API: Access the endpoints of your Flask REST API on the provided Heroku URL to ensure everything is working as expected.


That's it! Your Flask REST API should now be deployed on Heroku. You can continue to make changes to your app locally, commit them, and deploy updates to Heroku using the git push heroku master command.


---------------------------------------------------------------------------------

How to make requests to endpoints

Endpoints do not require authorization, there are two endpoints. 1 "/api/rider" this endpoint is in charge of receiving the following json
 {
    "rider_id": 3
}
which is composed by the reference "rider_id" with the id of the rider that is requesting the service as the value.

The endpoint will create the service by querying the database where the client location is located.

find the nearest available driver based on rider location

Driver status becomes occupied

and returns the following json as a successful answer

{
    "assigned_driver": {
        "id": 2,
        "lat_long": "(3.4762900227962774,-76.52684105709457)"
    },
    "message": "Ride created successfully",
    "ride_id": [
        39
    ]
}

2 "/api/driver" this endpoint is in charge of receiving the following json

{
    "ride_id": 39
}

which is composed of the reference "ride_id" with the id of the ride you want to terminate

and returns the following json as a successful answer

{
    "message": "ride completed successfully",
    "payment": "200 OK",
    "ride": {
        "arrive_lat_long": "(3.4762900227962774,-76.52684105709457)",
        "creation_date": "2023-05-17 15:24:04",
        "driver": 2,
        "finish_date": "2023-05-17 15:24:23",
        "id": 39,
        "origin_lat_long": "(3.452781936137825,-76.54903383590728)",
        "rider": 3,
        "state": "complete",
        "total_price": 708308
    }
}

confirming the value charged to the user, if the payment was successful or not and the final information of the closed service, changing the driver status to available again.
the driver's location is taken assuming that it is updated in real time, to make the final fare calculation example.
