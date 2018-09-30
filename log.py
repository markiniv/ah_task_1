import logging


def log(func):

    def wrapper(*args, **kwargs):
        logger.info("Program started")
        res = func(*args, **kwargs)
        logger.info("Done!")
        return res

    return wrapper


logger = logging.getLogger('test_log')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
fn = logging.FileHandler('log_task_1.log')
fn.setLevel(logging.DEBUG)
fn.setFormatter(formatter)

logger.addHandler(fn)
logger.setLevel(logging.DEBUG)
