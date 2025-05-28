# Install the latest version of Redis
!pip install -U redis

# Install LangChain and other required packages
!pip install -q langchain-community langchain-core unstructured

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
