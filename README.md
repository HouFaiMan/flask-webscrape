# flask-webscrape
A basic Flask application to webscrape a website.


# Application Setup
- Create a new project and a virtual environment for the application.
- Install the latest version of Flask.
- Rename the Python file to application.py.
- Install the following libraries using ```pip install``` command:
  
  [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Webscraping library for Python.
  
  [lxml](https://lxml.de/) - Processing library for XML and HTML in Python.
  
  [awscli](https://aws.amazon.com/cli/) - Amazon Web Services Command Line Interface.
  
  [requests](https://requests.readthedocs.io/en/master/) - Simple library for making HTTP requests.
  
  [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Amazon Web Services (AWS) SDK for Python.
  
  
- Import the installed libraries into the application and create a resource with a POST method to webscrape.
- Test the endpoint by sending a POST request locally using Postman.
  
# Elastic Beanstalk Deployment
- Go to AWS Management Console.
- Select the Elastic Beanstalk service.
- Click on "Create a new application" button.
- Fill in the application name and select the sample application option.
- Create the environment (setup takes a few minutes to complete).
- Configure the AWS credentials in terminal by running '''aws configure'''.
- Configure the session token in terminal by running '''aws configure set aws_session_token <ENTER_SESSION_TOKEN>'''
- Run '''pip freeze > requirements.txt'''
- Bundle the files into a zip file.
- Go back to Elastic Beanstalk, upload and deploy the application.
- Verify deployment by opening the URL or sending a request using Postman to the endpoint.

# Creating a DynamoDB table
- Go to AWS Management Console.
- Select DynamoDB service.
- Create a new table and fill in the table name and the primary key fields.

# Database functionality
- Import '''boto3''', find the DynamoDB resource and the newly created table.
- Create a new function to add new entries to the table.

# Deploy new version of application
- Bundle the files up into a zip file.
- Go back to Elastic Beanstalk service.
- Upload and deploy the application and change the versioning label.
- Verify deployment by sending a request using Postman to the endpoint.
- Go back to DynamoDB and verify the data have been upserted to the table.

# Restoring everything from scratch
- Select the DynamoDB service in AWS Management Console.
- Delete the table in DynamoDB.
- Select the Elastic Beanstalk service in AWS Management Console.
- Terminate the environment.
- Delete the application.

# Resources & Documentations
- [Deploy a Flask application to AWS.](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
- [Flask documentation.](https://flask.palletsprojects.com/en/1.1.x/)
- [Elastic Beanstalk documentation.](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)
- [DynamoDB documentation.](https://docs.aws.amazon.com/dynamodb/)
- [Webscraping sandbox.](http://toscrape.com/)
