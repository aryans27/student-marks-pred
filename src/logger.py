import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"      # name of the the file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)         # constructs path where log file will be stored. os.getcwd(): This gets the current working directory of the program
os.makedirs(logs_path,exist_ok=True)                # if folder already exists, continue with it, without throwing error

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,         # Sets the minimum level of messages to log. It's set to logging.INFO, meaning only messages at the INFO level or higher (e.g., WARNING, ERROR) will be recorded.
)

# testing if the logger is working
# if __name__=="__main__":      
#     logging.info("Logging has started")

