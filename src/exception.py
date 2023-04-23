import sys

def error_message_detail(error, error_detail:sys): # type: ignore
    _,_,exc_tb = error_detail.exc_info()
    error_message = 'error occured in python script [{0}] at line [{1}] error message [{2}]'.format( 
        exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(error) ) # type: ignore
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys): # type: ignore
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail = error_detail)

    def __str__(self):
        return self.error_message
