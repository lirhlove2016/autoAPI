
import logging
import logging.handlers
import datetime
import time
import threading
from conf.conf import reportDir,logDir

def get_logger():
    # output log
    now = time.strftime("%Y-%m-%d_%H_%M_%S", time.localtime(time.time()))
    logresult = logDir + r"/" + now + "_output.log"

    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)
    #输出到文件
    rf_handler = logging.handlers.TimedRotatingFileHandler(logresult , when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    # error log
    '''
    logresult_error = logDir + r"/" + now + "_error.log"

    f_handler = logging.FileHandler(logresult_error)
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
    '''
    logger.addHandler(rf_handler)
    #logger.addHandler(f_handler)

    return logger

if __name__=="__main__":
    logger=get_logger()
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')

