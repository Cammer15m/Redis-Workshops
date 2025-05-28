# Install the latest version of Redis (v5.0.1 as of June 2024)
!pip install -U redis

# Install LangChain and other required packages
!pip install -q langchain-community langchain-core unstructured langchain_openai

# Print Redis version for debugging
import redis
print(f"Redis version: {redis.__version__}")

# Add a small delay to ensure installation completes
import time
time.sleep(2)

# Start Redis Stack server
%%sh
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update > /dev/null 2>&1
sudo apt-get install redis-stack-server > /dev/null 2>&1
redis-stack-server --daemonize yes

# Verify Redis installation
!redis-cli ping

# Set up OpenAI API key
import os
from getpass import getpass

# Prompt for OpenAI API key if not already set
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass("Enter your OpenAI API key: ")
    
print("OpenAI API key is set")
