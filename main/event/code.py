from typing import NamedTuple


class Deal(NamedTuple):
    id: int
    type: str
    title: str
    body: str
    avatar: str
    percent: int
    bookingFor: str
    displayFor: str
    startAt: str
    expireAt: str
    excludedDates: str
    active: str


class SaveCode(NamedTuple):
    id: int
    firstname: str
    lastname: str
    phone: str
    email: str
    people: int
    arrivalTime: str
    note: str
    bookingCode: str
    voucherCode: str
    platform: str
    status: str
    createdAt: str
    updatedAt: str
    partnerId: str
    userId: int
    businessId: int
    deal: Deal
    placeId: int


class CodeUpdated(SaveCode):
    pass


class CodeCreated(SaveCode):
    pass
