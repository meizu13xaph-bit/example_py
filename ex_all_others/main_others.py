from config_log import ConfigLogger
from ex_all_others.dis_module import dis_mod

logF = ConfigLogger.get_logger("OnlyFile")

from ex_all_others.trap_task import trap_1
from ex_all_others.dis_async_await import async_start
from ex_all_others.rich_print import rich_console_text
from ex_all_others.closure_func import closure_start, closure_new1
from ex_all_others.deep_copy_example import deep_start
from ex_all_others.sobes11 import not_hash_err, sob_work_1
from ex_all_others.others_11 import others_11_start


# ------------------------------------------------------------------------
def main_others(w=None):
    if w is not None:  # w=None
        return
    logF.info(f"'****' main_others - 'start'")

    # trap_1()
    # async_start()
    # rich_console_text()
    # closure_start()
    # deep_start()

    # not_hash_err()
    # sob_work_1()
    # others_11_start()
    # closure_new1()
    dis_mod()
