from typing import List, Any, Optional
from datetime import datetime
from ninja import Schema
from pydantic import EmailStr


class WaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: EmailStr

class ErrorWaitlistEntryCreateSchema(Schema):
    # Create -> Data
    # WaitlistEntryIn
    email: List[Any]
    # non_field_errors: List[dict] = []


class WaitlistEntryListSchema(Schema):
    # List -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
    description: Optional[str] = ""


class WaitlistEntryDetailSchema(Schema):
    # Get -> Data
    # WaitlistEntryOut
    id: int
    email: EmailStr
    updated: datetime
    timestamp: datetime
    description: Optional[str] = ""


class WaitlistEntryUpdateSchema(Schema):
    # Put -> Data
    # WaitlistEntryOut
    # id: int
    description: str = ""