from pydantic import BaseModel, Field
from typing import Optional, List

class BoundingBox(BaseModel):
    ymin: int
    xmin: int
    ymax: int
    xmax: int

class KYCDocumentSchema(BaseModel):
    full_name: Optional[str] = Field(default=None, description="Full legal name on the identity document")
    id_number: Optional[str] = Field(default=None, description="Unique ID number (e.g., Driver's License/Passport)")
    date_of_birth: Optional[str] = Field(default=None, description="Date of Birth in YYYY-MM-DD format")
    issue_date: Optional[str] = Field(default=None, description="Date of Issue in YYYY-MM-DD format")
    expiry_date: Optional[str] = Field(default=None, description="Expiry date of the document")
    bbox_id_number: Optional[List[int]] = Field(default=None, description="Normalized coordinates [ymin, xmin, ymax, xmax]")