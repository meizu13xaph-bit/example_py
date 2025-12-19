from config_log import ConfigLogger

logF = ConfigLogger.get_logger("OnlyFile")

from ex_file_zip import simple_zip


def run_file_zip(w=None):
    if w is not None:  # w=None
        return
    logF.info(f"'****' main_file_zip - 'start'")

    simple_zip.write_to_zip()
