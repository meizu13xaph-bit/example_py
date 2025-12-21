from config_log import ConfigLogger

logF = ConfigLogger.get_logger("OnlyFile")

import json
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path


DIR_CWD: Path = Path.cwd()
DIR_CURRENT_FILE: Path = Path(__file__).resolve().parent

NAME_DIR_FILES: str = "zip_files_dir/"
DIR_FILES: Path = DIR_CURRENT_FILE / NAME_DIR_FILES


def write_to_zip_no_temp():
    """
    1. Создает ZIP-архив и добавляет в него файл напрямую из памяти,
       без создания временного файла.
    2. Записывает JSON данные напрямую в архив с помощью writestr.
    """
    logF.info(f"Absolute paths: {DIR_CWD=} \n{DIR_CURRENT_FILE=}")
    logF.info(f"Absolute paths: {NAME_DIR_FILES=} \n{DIR_FILES=}")
    # Создаем директорию, куда будут сохраняться файлы, если она не существует
    DIR_FILES.mkdir(parents=True, exist_ok=True)

    # Открываем менеджер контекста для создания ZIP-архива
    zip_path = DIR_FILES / "zip_no_temp.zip"
    with ZipFile(
        zip_path,
        "w",
        compression=ZIP_DEFLATED,
        compresslevel=9,
    ) as open_zip:
        data: dict = {"a": "1", "b": "2", "method": "writestr"}
        # Записываем JSON данные напрямую в архив под именем 'json_no_temp.json'
        # writestr принимает имя файла в архиве и данные (строка или байты)
        open_zip.writestr("json_no_temp1.json", json.dumps(data))
        open_zip.writestr("json_no_temp2.json", json.dumps(data))
