from sqlalchemy.orm import Session

from app.db import get_engine
from app.models.base import Base
from app.models.job import Job
from app.models.skills import Skill
from app.models.language import Language

from sqlalchemy import Engine


def main() -> None:

    engine: Engine = get_engine()

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        session.add(
            Job(
                title="Junior Backend Developer",
                company="Acme",
                url="https://example.com/jobs/1",
                raw_text="We are looking for a junior dev with Python and SQL",
                source="manual",
            )
        )

        session.commit()


if __name__ == "__main__":
    main()
