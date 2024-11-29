from pydantic import BaseModel, Extra
from typing import Optional


class Config(BaseModel, extra=Extra.ignore):
    # Your Config Here
    help_block: Optional[bool] = False
    help_priority: Optional[int] = 1
    help_ignore_plugins: Optional[list] = []
    help_to_me: Optional[bool] = False
    help_specific_bots: Optional[list] = []
