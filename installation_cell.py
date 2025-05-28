# Install Redis with search capabilities
!pip install "redis>=4.5.1"

# Install LangChain and other required packages
!pip install -q langchain-community langchain-core unstructured

# Add a small delay to ensure installation completes
import time
time.sleep(2)

# Additionally, you need to have Redis server with search module running
# The notebooks use this command to install and start Redis Stack server:
%%sh
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update > /dev/null 2>&1
sudo apt-get install redis-stack-server > /dev/null 2>&1
redis-stack-server --daemonize yes
