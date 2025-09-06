from config_log import ConfigLogger
from ex_code_war.main_code_war import main_code_war

ConfigLogger.setting_path_logger(log_file="example.log")
logF = ConfigLogger.get_logger("OnlyFile")
logFC = ConfigLogger.get_logger("FileStdout")

from ex_metaclass import main_metaclass
from ex_all_others import main_others

# source venv/bin/activate
# venv\Scripts\activate


def main():
    main_metaclass.main_metaclass(0)
    main_others.main_others()
    main_code_war(0)

    logFC.warning("end '-------------------examplePY - main()' '---------------------------------'\n\n\n\n"
                 "'*******************************************************************************'")


if __name__ == '__main__':
    main()
