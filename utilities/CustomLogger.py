import inspect
import logging
import allure


def customLogger():

    logName = inspect.stack()[1][3]

    # Create the logging object
    logger = logging.getLogger(logName)

    # Set the Log level
    logger.setLevel(logging.DEBUG)

    # fileHandler create
    fileHandler = logging.FileHandler('reports/app_logs.log', mode='a')

    # Set the logLevel for fileHandler
    fileHandler.setLevel(logging.DEBUG)

    # Create the formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # Set the formatter to fileHandler
    fileHandler.setFormatter(formatter)

    # Add file handler to logging
    logger.addHandler(fileHandler)

    return logger


def allureLogs(text):
    with allure.step(text):
        pass
