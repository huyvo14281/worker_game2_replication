from sqlalchemy import *

from model.base import Base


class Code(Base):
    __tablename__ = 'code'
    id = Column(BigInteger, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    phone = Column(String)
    email = Column(String)
    arrivalTime = Column(String)
    note = Column(String)
    bookingCode = Column(String)
    voucherCode = Column(String)
    platform = Column(String)
    status = Column(String)
    createdAt = Column(String)
    updatedAt = Column(String)
    partnerId = Column(String)
    userId = Column(String)
    businessId = Column(String)
    placeId = Column(BigInteger)
