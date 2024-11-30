from pydantic import BaseModel, Extra
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    # Your Config Here
    picmenu_block: Optional[bool] = False
    picmenu_priority: Optional[int] = 1
    picmenu_ignore_plugins: Optional[list] = []
    picmenu_to_me: Optional[bool] = False
