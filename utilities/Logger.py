import logging
class Log_generation_class:

    @staticmethod
    def log_gen_method():
        log_file=logging.FileHandler(".\\Logs\\CredKart_Automation_Testing.log")
        log_format=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')
        log_file.setFormatter(log_format)
        logger=logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger


