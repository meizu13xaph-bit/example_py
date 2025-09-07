from config_log import ConfigLogger

ConfigLogger.setting_path_logger(log_file="example.log")
logF = ConfigLogger.get_logger("OnlyFile")
logFC = ConfigLogger.get_logger("FileStdout")

from ex_metaclass import main_metaclass
from ex_all_others import main_others
from ex_code_war import main_code_war
from ex_library import main_library

# source venv/bin/activate
# venv\Scripts\activate


def main():
    main_metaclass.main_metaclass(0)
    main_others.main_others(0)
    main_code_war.code_war_1(0)
    main_library.main_library()

    logFC.warning(
        "end '-------------------examplePY - main()' '---------------------------------'\n\n\n\n"
        "'*******************************************************************************'"
    )


if __name__ == "__main__":
    main()
