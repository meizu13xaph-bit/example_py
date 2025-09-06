from config_log import ConfigLogger
logF = ConfigLogger.get_logger("OnlyFile")

from ex_code_war.split_strings import split_strings


# ------------------------------------------------------------------------
def main_code_war(w=None):
    if w is not None:  # w=None
        return
    logF.info(f"'****' main_code_war - 'start'")

    print(10 or 5 * 7)

    a = [1, 2, 3]
    b = [4, 5, 6]
    print(f"{id(a)} - {id(b)}")

    # a = a + b
    # a = a.__add__(b)
    # a += b
    # a.__iadd__(b)
    # a + b
    # a.__add__(b)

    b = a.__iadd__(b)
    print(f"{id(a)} - {id(b)}")
    print(a)

    split_strings()
