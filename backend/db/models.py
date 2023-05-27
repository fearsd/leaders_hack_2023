import enum
from datetime import date as _date, datetime, time
from typing import Optional, List, Set
from sqlalchemy.sql import func
from sqlalchemy import Column, Date, DateTime, Time, Integer
from sqlalchemy.dialects.postgresql import JSON, ARRAY

from sqlmodel import SQLModel, Field, Enum, Relationship

class Gender(str, enum.Enum):
    male = "Мужчина"
    female = "Женщина"


class CategoryBase(SQLModel):
    name: str


class Category(CategoryBase, table=True):
    id: int = Field(default=None, primary_key=True)
    routes: List["Route"] = Relationship(back_populates="category")


class LevelBase(CategoryBase):
    old_id: int


class Level1(LevelBase, table=True):
    id: int = Field(default=None, primary_key=True)
    routes: List["Route"] = Relationship(back_populates="level1")


class Level2(LevelBase, table=True):
    id: int = Field(default=None, primary_key=True)
    routes: List["Route"] = Relationship(back_populates="level2")



class ScheduleBase(SQLModel):
    is_active: bool
    group_old_id: int
    is_planned: bool
    body: str


class Schedule(ScheduleBase, table=True):
    id: int = Field(default=None, primary_key=True)
    group_id: Optional[int] = Field(default=None, foreign_key="group.id")
    group: Optional["Group"] = Relationship(back_populates="schedules")


class DistrictBase(SQLModel):
    name: str


class District(DistrictBase, table=True):
    id: int = Field(default=None, primary_key=True)
    addresses: List["Address"] = Relationship(back_populates="district")


class Municipal(DistrictBase, table=True):
    id: int = Field(default=None, primary_key=True)
    addresses: List["Address"] = Relationship(back_populates="municipal")


class AddressBase(SQLModel):
    address: str
    group_old_ids: List[int] = Field(sa_column=Column(ARRAY(Integer())))

class GroupAddressLink(SQLModel, table=True):
    group_id: Optional[int] = Field(
        default=None, foreign_key="group.id", primary_key=True
    )
    address_id: Optional[int] = Field(
        default=None, foreign_key="address.id", primary_key=True
    )

class Address(AddressBase, table=True):
    id: int = Field(default=None, primary_key=True)
    district_id: Optional[int] = Field(default=None, foreign_key="district.id")
    district: Optional[District] = Relationship(back_populates="addresses")

    municipal_id: Optional[int] = Field(default=None, foreign_key="municipal.id")
    municipal: Optional[Municipal] = Relationship(back_populates="addresses")

    groups: List["Group"] = Relationship(back_populates="addresses", link_model=GroupAddressLink)



class RouteBase(SQLModel):
    old_id: int
    name: str
    is_online: bool
    description: str


class Route(RouteBase, table=True):
    id: int = Field(default=None, primary_key=True)
    category_id: int = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="routes")

    level1_id: int = Field(default=None, foreign_key="level1.id")
    level1: Optional[Level1] = Relationship(back_populates="routes")

    level2_id: int = Field(default=None, foreign_key="level2.id")
    level2: Optional[Level2] = Relationship(back_populates="routes")
    groups: List["Group"] = Relationship(back_populates="route")


class UserBase(SQLModel):
    old_id: int
    birthday: _date = Field(
        sa_column=Column(Date())
    )
    address: str
    gender: Gender = Field(sa_column=Column(Enum(Gender)))
    datetime_created: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    firstname: Optional[str]
    lastname: Optional[str]
    patronymic: Optional[str]


class UserAccount(UserBase, table=True):
    id: int = Field(default=None, primary_key=True)
    attendances: List["Attendance"] = Relationship(back_populates="useraccount")


class GroupBase(SQLModel):
    old_id: int

class Group(GroupBase, table=True):
    id: int = Field(default=None, primary_key=True)
    route_id: int = Field(default=None, foreign_key="route.id")
    route: Optional[Route] = Relationship(back_populates="groups")

    addresses: List["Address"] = Relationship(back_populates="groups", link_model=GroupAddressLink)
    schedules: List["Schedule"] = Relationship(back_populates="group")
    attendances: List["Attendance"] = Relationship(back_populates="group")


class AttendanceBase(SQLModel):
    old_id: int
    is_online: bool
    date: _date = Field(
        sa_column=Column(Date())
    )
    time_start: time = Field(
        sa_column=Column(Time(timezone=True))
    )
    time_end: time = Field(
        sa_column=Column(Time(timezone=True))
    )


class Attendance(AttendanceBase, table=True):
    id: int = Field(default=None, primary_key=True)
    group_id: int = Field(default=None, foreign_key="group.id")
    group: Group = Relationship(back_populates="attendances")

    useraccount_id: int = Field(default=None, foreign_key="useraccount.id")
    useraccount: UserAccount = Relationship(back_populates="attendances")
