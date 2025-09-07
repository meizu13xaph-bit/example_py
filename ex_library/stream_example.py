from config_log import ConfigLogger
from ex_library.stream import Stream

logF = ConfigLogger.get_logger("OnlyFile")

def run_my_stream_example():
    numbers = [2, 3, 4, 5, 6]

    def flatMap_func(param):
        return param, param + 1

    result = (
        Stream(numbers)
        .map(lambda x: x**2)
        .flatMap(flatMap_func)
        .filter(lambda x: x <= 36)
        .map(str)
        .to_list()
    )
    logF.info(f"My Stream result: {result}")

if __name__ == "__main__":
    run_my_stream_example()
