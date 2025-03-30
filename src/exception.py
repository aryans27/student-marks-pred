import sys
from src.logger import logging

def error_msg_detail(error, error_detail:sys):      # sys module itself is passed as a parameter so we can use sys.exc_info() to get the traceback info.
    _,_,exc_tb = error_detail.exc_info()        # gives the execution info
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = "Error occured in python script name [{0}], line no: [{1}] error__message: [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_msg


class CustomException(Exception):
    def __init__(self, error_msg, error_detail:sys):
        super().__init__(error_msg)
        self.error_msg = error_msg_detail(error_msg, error_detail = error_detail)

    def __str__(self):
        return self.error_msg 

# Test case
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:                                            # except clause can be used to catch any kind of exceptions thrown by python scripts or other programs written using python programming language.
        logging.info("Divide by Zero")
        raise CustomException(e,sys)  