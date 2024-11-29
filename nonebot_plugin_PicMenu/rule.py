from nonebot.internal.rule import Rule
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot import get_driver
from nonebot.rule import to_me

from .config import Config

plugin_config = Config.parse_obj(get_driver().config)


def isInBotList(bots: list) -> Rule:
    async def _enable(event: MessageEvent) -> bool:
        if str(event.self_id) in bots:
            return True
        return False
    return Rule(_enable)


if len(plugin_config.help_specific_bots) > 0:
    if plugin_config.help_to_me:
        help_rule = isInBotList(plugin_config.help_specific_bots) & to_me()
    else:
        help_rule = isInBotList(plugin_config.help_specific_bots)
else:
    help_rule = to_me() if plugin_config.help_to_me else None
