from config import config
from sqlalchemy import Column, MetaData, ForeignKey, DateTime, Text, Integer,text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base(metadata=MetaData(schema=config.APP_SCHEMA))
Base = declarative_base()


def generate_fk_name(table_name: str, column_name: str) -> str:
    fk_name = f"{table_name}_{column_name}_fkey"
    return fk_name[:63]

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='ID задачи')
    title: Mapped[str] = mapped_column(Text, nullable=False, comment='Свойства задачи')
    description: Mapped[str] = mapped_column(Text, nullable=False, comment='Описание задачи')
    status: Mapped[str] = mapped_column(
        ForeignKey('status.name', name=generate_fk_name(__tablename__, "status")),
        nullable=False,
        comment='Статус задачи',
        default = 'new'
    )
    created_at = Column(DateTime(timezone=True), comment='Когда создалась задача', server_default=text("CURRENT_TIMESTAMP"))
    
class Status(Base):
    __tablename__ = "status"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment='ID статуса')
    name: Mapped[str] = mapped_column(Text, nullable=False, comment='Название статуса')
    description: Mapped[str] = mapped_column(Text, nullable=False, unique=True, comment='Описание статуса')