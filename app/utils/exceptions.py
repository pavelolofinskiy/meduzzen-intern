from starlette import status
from starlette.exceptions import HTTPException


class UserFoundError(HTTPException):
    def init(self, id: int):
        super().init(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} doesn't exists.")

