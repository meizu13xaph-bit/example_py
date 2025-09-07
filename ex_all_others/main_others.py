from config_log import ConfigLogger

logF = ConfigLogger.get_logger("OnlyFile")

from ex_all_others import trap_task
from ex_all_others import dis_async_await
from ex_all_others import rich_print
from ex_all_others import closure_func
from ex_all_others import deep_copy_example
from ex_all_others import sobes11
from ex_all_others import others_11
from ex_all_others import dis_module


# ------------------------------------------------------------------------
def main_others(w=None):
    if w is not None:  # w=None
        return
    logF.info(f"'****' main_others - 'start'")

    # trap_task.trap_1()
    dis_async_await.async_start()
    rich_print.rich_console_text()

    closure_func.closure_start()
    closure_func.closure_new1()

    # deep_copy_example.deep_start()

    # sobes11.not_hash_err()
    # sobes11.sob_work_1()

    # others_11.others_11_start()
    # dis_module.dis_mod()
