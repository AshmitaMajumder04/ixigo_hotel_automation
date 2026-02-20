import logging

def get_logger():

    logger = logging.getLogger("ixigo")


    if not logger.handlers:

        logger.setLevel(logging.INFO)

        handler = logging.FileHandler("reports/test.log", mode="a")

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger