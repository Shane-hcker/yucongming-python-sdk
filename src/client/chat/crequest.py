# -*- encoding: utf-8 -*-
from typing import *
import json


class DevChatRequest:
    """AI对话请求"""
    def __init__(self, model_id=None, message=None):
        self.model_id = model_id
        self.message = message

    def toJsonString(self) -> str:
        if not (self.model_id or self.message):
            raise InterruptedError('AI Model ID or message hasn\'t been setup yet')
        return json.dumps(dict(modelId=self.model_id, message=self.message))
