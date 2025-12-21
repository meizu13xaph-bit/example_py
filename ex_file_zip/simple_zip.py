from config_log import ConfigLogger

logF = ConfigLogger.get_logger("OnlyFile")

import json
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path


DIR_CWD: Path = Path.cwd()
DIR_CURRENT_FILE: Path = Path(__file__).resolve().parent

NAME_DIR_FILES: str = "zip_files_dir/"
DIR_FILES: Path = DIR_CURRENT_FILE / NAME_DIR_FILES


def write_to_zip():
    """
    1. Создает новый ZIP-архив с максимальным сжатием.
    2. Создает на диске временный JSON файл.
    3. Записывает этот JSON файл в архив под именем 'json1.json'.
    """
    # Логируем текущие пути для отладки
    logF.info(f"Absolute paths: {DIR_CWD=} \n{DIR_CURRENT_FILE=}")
    logF.info(f"Absolute paths: {NAME_DIR_FILES=} \n{DIR_FILES=}")

    # Создаем директорию, куда будут сохраняться файлы, если она не существует
    DIR_FILES.mkdir(parents=True, exist_ok=True)

    # Открываем менеджер контекста для создания ZIP-архива
    # compression=ZIP_DEFLATED: используем стандартный алгоритм сжатия
    # compresslevel=9: устанавливаем максимальный уровень сжатия
    with ZipFile(
        DIR_FILES / "zip_with_temp.zip",
        "w",
        compression=ZIP_DEFLATED,
        compresslevel=9,
    ) as open_zip:
        # Создаем на диске временный JSON файл для последующего добавления
        with open(DIR_FILES / "temp_json1.json", "w") as open_json:
            data: dict = {"a": "1", "b": "2", "method": "writestr"}
            # Записываем данные в 'temp_json1.json' файл
            json.dump(data, open_json)

        # Добавляем созданный файл 'temp_json1.json' с диска в архив
        # arcname указывает имя файла, которое будет внутри архива
        open_zip.write(DIR_FILES / "temp_json1.json", arcname="json1.json")
