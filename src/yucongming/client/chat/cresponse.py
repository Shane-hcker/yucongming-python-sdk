# -*- encoding: utf-8 -*-
from typing import *
import json


class DevChatResponse:
    def __init__(self, byte_json: bytes):
        # self.message = None
        # self.code = None
        # self.data = None
        self.stuff = None
        if not byte_json:
            return
        self.__map_json(byte_json)

    @property
    def content(self) -> Tuple[int, Any, str]:
        return self.stuff

    def __map_json(self, byte_json: bytes) -> None:
        self.stuff = json.loads(byte_json).values()
