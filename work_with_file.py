import logging
import json
import csv


def read_settings(settings: str) -> dict:
    """the function reads values from settings.json"""
    try:
        with open(settings) as json_file:
            settings = json.load(json_file)
        logging.info(
            f"the data of settings successfully read")
    except Exception as e:
        logging.warning(
            f"an error occurred when reading data to '{settings}' file: {str(e)}")
    return settings


def write_settings(settings: dict, path_settings: str) -> None:
    """the function writes values to settings.json"""
    try:
        with open(path_settings, 'w') as f:
            json.dump(settings, f)
        logging.info(
            f"the data of settings successfully write")
    except Exception as e:
        logging.warning(
            f"an error occurred when writing data to '{settings}' file: {str(e)}")


def read_statistic(path_file_name: str) -> dict:
    """the function reads data from a csv-file"""
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


def write_statistic(time: float, pool: int, path_file_name: str) -> None:
    """the function writes data to a csv-file"""
    try:
        with open(path_file_name, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([pool, time])
        logging.info("statistics successfully write")
    except Exception as e:
        logging.warning(
            f"an error occurred when writing data to '{path_file_name}' file: {str(e)}")
