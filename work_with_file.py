import logging

def write_file(path_file_name: str, data: str):
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        with open(path_file_name, "w") as f:
            f.write(data)
        logging.info(f"the data was successfully written to the file: {path_file_name}")
    except Exception as e:
        logging.error(f"an error occurred when writing data to '{path_file_name}' file: {str(e)}")
        raise Exception("error")
    
def read_file(path_file_name: str):
    logging.basicConfig(level=logging.INFO, filename="py_log.log")
    try:
        with open(path_file_name, "r") as f:
            text = f.read()
        logging.info(f"the data was successfully read to the file: {path_file_name}")
        return text
    except Exception as e:
        logging.error(f"an error occurred when reading data to '{path_file_name}' file: {str(e)}")
        raise Exception("error")
