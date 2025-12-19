from config_log import ConfigLogger

logF = ConfigLogger.get_logger("OnlyFile")

import json
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path


DIR_CWD: Path = Path.cwd()
DIR_CURRENT_FILE: Path = Path(__file__).resolve().parent

NAME_DIR_FILES: str = "zip_files_dir"
DIR_FILES = DIR_CURRENT_FILE / NAME_DIR_FILES


def write_to_zip():
    """
    Создает ZIP-архив и добавляет в него JSON файл.

    Функция выполняет следующие действия:
    1. Создает директорию для файлов, если она не существует.
    2. Создает новый ZIP-архив с максимальным сжатием.
    3. Генерирует временный JSON файл.
    4. Записывает этот JSON файл в архив под именем 'json1.json'.
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
        DIR_FILES / "zip1.zip",
        "w",
        compression=ZIP_DEFLATED,
        compresslevel=9,
    ) as open_zip:
        # Создаем временный JSON файл для последующего добавления в архив
        with open(DIR_FILES / "temp_json1.json", "w") as open_json:
            json.dump({"a": "1", "b": "2"}, open_json)
            open_json.seek(0)  # Сброс курсора (хотя для записи по пути ниже это не критично)

            # Добавляем созданный файл в архив
            # arcname указывает имя файла, которое будет внутри архива
            open_zip.write(DIR_FILES / "temp_json1.json", arcname="json1.json")
