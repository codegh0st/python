
#----------------------
# HANDLING SENSITIVE DATA IN PYTHON - Uing Environment Varaibles
#----------------------
'''
Ensure .env is Not Committed to Version Control
Add .env to your .gitignore file to ensure it is not included in version control.
NOTE: i am DELIBERATLY Commiting .env to versin control, so that i can understand the concept/how env work in pyhton easily.

# .gitignore
.env

#-----------------------

How load_dotenv Works

1.Read the .env File: The load_dotenv function reads the .env file located in your project directory. This file typically contains key-value pairs, with each pair on a new line. For example:
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here
API_KEY=your_api_key_here

Set Environment Variables: The function sets these key-value pairs as environment variables in the Python process. This means that after calling load_dotenv, you can access these values using os.getenv or directly from the os.environ dictionary.

Example with Explanation
Here's the script again with detailed comments to explain each step:
# config.py
import os
from dotenv import load_dotenv

# By Default Loads environment variables from the .env file
load_dotenv()
# The above function reads the .env file and sets the environment variables
# defined in it. These variables are then available in the Python environment.

# Access the variables
SECRET_KEY = os.getenv('SECRET_KEY')
# Retrieves the value of 'SECRET_KEY' from the environment variables

DATABASE_URL = os.getenv('DATABASE_URL')
# Retrieves the value of 'DATABASE_URL' from the environment variables

API_KEY = os.getenv('API_KEY')
# Retrieves the value of 'API_KEY' from the environment variables

print(f"SECRET_KEY: {SECRET_KEY}")
# Prints the value of 'SECRET_KEY' to ensure it is loaded correctly

print(f"DATABASE_URL: {DATABASE_URL}")
# Prints the value of 'DATABASE_URL' to ensure it is loaded correctly

print(f"API_KEY: {API_KEY}")
# Prints the value of 'API_KEY' to ensure it is loaded correctly



#-----------------------



'''


#----------------------
# EXAMPLE: WORKING WITH MULTIPLE ENVIONMENT WITH ITS OWN SEPERATE CONFIGURATIONS

# Create .env Files According to the Environments

# .env.dev
SECRET_KEY=dev_secret_key
DATABASE_URL=dev_database_url
API_KEY=dev_api_key

# .env.test
SECRET_KEY=test_secret_key
DATABASE_URL=test_database_url
API_KEY=test_api_key


# Main Configuration Script which will work on all environment
# config.py
import os
from dotenv import load_dotenv

# Determine the environment (default to 'dev' if not set)
ENV = os.getenv('ENV', 'dev') #if user sets Environment varable 'export ENV=test' value,script will take value form '.env.test' file , if not , if user doesn’t provide ‘dev’ will be taken in ‘ENV’

# Load the appropriate .env file based on the current environment
dotenv_file = f".env.{ENV}" # Fetching Value set by user, in environment var 'ENV', foramting that value in string such a way that it matches my configuration-file name eg.(.env.dev or .env.test), and giving it to 'load_dontenv' function,
load_dotenv(dotenv_file) # creaing environment variable from .env.dev or .env.test, whatever is provided by user

# Access the variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

print(f"Environment: {ENV}")
print(f"SECRET_KEY: {SECRET_KEY}")
print(f"DATABASE_URL: {DATABASE_URL}")
print(f"API_KEY: {API_KEY}")

# # Set the Environment Variable and Run the Script

# For development environment:
# export ENV=dev
# python config.py


# For testing environment:
# export ENV=test
# python config.py


#----------------------
# Example: Using Environment Variables with python-dotenv
# .env
SECRET_KEY=your_secret_key_here
DATABASE_URL=your_database_url_here
API_KEY=your_api_key_here



# config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the variables
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

print(f"SECRET_KEY: {SECRET_KEY}")
print(f"DATABASE_URL: {DATABASE_URL}")
print(f"API_KEY: {API_KEY}")
#----------------------



