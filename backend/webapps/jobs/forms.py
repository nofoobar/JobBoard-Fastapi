from typing import List
from typing import Optional

from fastapi import Request


class JobCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.company: Optional[str] = None
        self.company_url: Optional[str] = None
        self.location: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get("title")
        self.company = form.get("company")
        self.company_url = form.get("company_url")
        self.location = form.get("location")
        self.description = form.get("description")

    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("A valid title is required")
        if not self.company_url or not (self.company_url.__contains__("http")):
            self.errors.append("Valid Url is required e.g. https://example.com")
        if not self.company or not len(self.company) >= 1:
            self.errors.append("A valid company is required")
        if not self.description or not len(self.description) >= 20:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False
