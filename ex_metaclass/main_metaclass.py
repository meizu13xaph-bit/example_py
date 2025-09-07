from config_log import ConfigLogger

logF = ConfigLogger.get_logger("OnlyFile")

from ex_metaclass import metaclass_mul_call

# from ex_metaclass import noisy_meta


# ------------------------------------------------------------------------
def main_metaclass(w=None):
    if w is not None:  # w=None
        return
    logF.info(f"'****' main_metaclass - 'start'")

    metaclass_mul_call.mul_func_descriptor()
    # noisy_meta.start_noisy_meta()
