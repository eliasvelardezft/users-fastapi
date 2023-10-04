from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.base import Base


class Profile(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String)
    last_name: Mapped[str] = mapped_column(String)
    birthdate: Mapped[datetime] = mapped_column(DateTime)
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('user.id'), index=True)    
    user: Mapped = relationship("User", back_populates="profile")
