# -*- encoding: utf-8 -*-
from typing import *
import json


class DevChatResponse:
    def __init__(self, byte_json: bytes):
        self.message = None
        self.code = None
        self.data = None
        if not byte_json:
            return
        self.__map_json(byte_json)

    @property
    def content(self) -> Tuple[int, Any, str]:
        return self.code, self.data, self.message

    def __map_json(self, byte_json: bytes) -> None:
        self.code, self.data, self.message = json.loads(byte_json).values()
