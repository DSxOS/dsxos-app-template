import query_utils
import argparse
import yaml
from datetime import datetime, timezone
import pytz
from logger import setup_logger

#######################################################################
#### INITIALIZATION
#######################################################################
APP_NAME = "dsxos-app-test"

# Create parser
parser = argparse.ArgumentParser(description=f"Run {APP_NAME} with config file")
parser.add_argument("-c", "--config", required=False, help="Path to config YAML file", default="/app/config.yaml")
args = parser.parse_args()
with open(args.config, "r") as f: 
    raw_data = yaml.safe_load(f)
    
# Extract API URL and Token
api_url = raw_data['params']['apiEndpoint']
api_token = raw_data['params']['token']
api_headers = {"Authorization": api_token}

# Initialize logger with central logging to Loki
logger = setup_logger(
    log_file="query.log",
    loki_url="http://localhost:3100/loki/api/v1/push",  # Loki address
    loki_tags={"app_name": APP_NAME},        # add more tags if needed
    level=raw_data["logLevel"]    
)

# Initialize query_utils with URL + headers    
query_utils.init(api_url, api_headers, logger)

# Log passed arguments for debugding
logger.debug(f"{APP_NAME} run with arguments: %s", raw_data)

#######################################################################
#### APPLICATION
#######################################################################
try:
    # Your application logger with exception handling
    
except Exception as e:
    # Exception handling
    # logger.error(f'Error generating ESS schedule: {e}')

#######################################################################
#### FINALIZATION
#######################################################################
logger.info(f"{APP_NAME} executed successfully")
