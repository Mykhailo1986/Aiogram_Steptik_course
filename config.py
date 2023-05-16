from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Access specific variables
TOKEN: str = env_vars['BOT_TOKEN']
