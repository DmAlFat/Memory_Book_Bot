from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Page(Base):
    __tablename__ = 'pages'

    id: Mapped[int] = mapped_column(primary_key=True)
    surname: Mapped[str] = mapped_column(String())
    name: Mapped[str] = mapped_column(String())
    patronymic: Mapped[str] = mapped_column(String())
    birthday: Mapped[str] = mapped_column(String())
    birthplace: Mapped[str] = mapped_column(String())
    death_date: Mapped[str] = mapped_column(String())
    death_place: Mapped[str] = mapped_column(String())
    biography: Mapped[str] = mapped_column(String())
    obit: Mapped[str] = mapped_column(String())

    def __str__(self):
        return f"Фамилия: {self.surname}\n" \
               f"Имя: {self.name}\n" \
               f"Отчество: {self.patronymic}\n" \
               f"Дата рождения: {self.birthday}\n" \
               f"Место рождения: {self.birthplace}\n" \
               f"Дата смерти: {self.death_date}\n" \
               f"Место смерти: {self.death_place}\n" \
               f"Биография: {self.biography}\n" \
               f"Эпитафия: {self.obit}\n"


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
