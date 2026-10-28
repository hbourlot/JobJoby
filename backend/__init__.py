import sqlalchemy as sa
from app.db import *


def main() -> None:

    engine: sa.Engine = get_engine()
    metadata: sa.MetaData = sa.MetaData()

    return None


if __name__ == "__main__":
    main()
