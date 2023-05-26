import logging
import csv


def write_file(path_file_name: str, data: str) -> None:
    """the function writes text data to a file"""
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        with open(path_file_name, "w") as f:
            f.write(data)
        logging.info(
            f"the data was successfully written to the file: {path_file_name}")
    except Exception as e:
        logging.error(
            f"an error occurred when writing data to '{path_file_name}' file: {str(e)}")
        raise Exception("error")


def read_file(path_file_name: str) -> str:
    """the function reads text data from a file"""
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        with open(path_file_name, "r") as f:
            text = f.read()
        logging.info(
            f"the data was successfully read to the file: {path_file_name}")
        return text
    except Exception as e:
        logging.error(
            f"an error occurred when reading data to '{path_file_name}' file: {str(e)}")
        raise Exception("error")


def read_statistic(path_file_name: str) -> dict:
    """the function reads data from a csv-file"""
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        with open(path_file_name, 'r') as f:
            reader = csv.reader(f)
            statistic = list(reader)
        result = {}
        for i in statistic:
            pool, time = i
            result[int(pool)] = float(time)
        logging.info("statistics successfully read")
        return result
    except Exception as e:
        logging.error(
            f"an error occurred when reading data to '{path_file_name}' file: {str(e)}")
        raise Exception("error")


def write_statistic(time: float, pool: int, path_file_name: str) -> None:
    """the function writes data to a csv-file"""
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        with open(path_file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([pool, time])
        logging.info("statistics successfully write")
    except Exception as e:
        logging.warning(
            f"an error occurred when reading data to '{path_file_name}' file: {str(e)}")
