import sys

def error_message_details(error, detail:sys):
    _, _, exc_tb = detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_numb = exc_tb.tb_lineno
    error_message = f"Error occured in python script name [{file_name}] line number [{line_numb}] error message {str(error)}"
    
    return error_message

class CustomException(Exception):
    
    def __init__(self, error_message, detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, detail=detail)

    def __str__(self):
        return self.error_message
