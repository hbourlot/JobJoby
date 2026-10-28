import sqlalchemy as sa
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

FILE_PATH = Path(__file__).resolve().parents[2] / ".secrets" / "postgres_password.txt"


def get_password(f_path: Path) -> str:
    print(f_path)
    return f_path.read_text().strip()


def get_engine() -> sa.Engine:

    url = sa.URL.create(
        os.environ["DRIVER_NAME"],
        os.environ["POSTGRES_USER"],
        # os.environ["POSTGRES_PASSWORD"],
        get_password(FILE_PATH),
        os.environ["HOST"],
        int(os.environ["POSTGRES_PORT"]),
        os.environ["POSTGRES_DB"],
    )

    return sa.create_engine(url, echo=False)
