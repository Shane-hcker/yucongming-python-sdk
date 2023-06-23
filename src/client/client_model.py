# -*- encoding: utf-8 -*-
from typing import *
import json
import requests
import hashlib

from .chat.crequest import *
from .chat.cresponse import *


class YCMClient:
    def __init__(self, accessKey=None, secretKey=None):
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.host: Final = 'https://www.yucongming.com/api/dev'

    def getHeaderDict(self, body) -> dict:
        if not (self.accessKey or self.secretKey):
            raise InterruptedError('access key or secret key hasn\'t been setup yet')
        return dict(
            accessKey=self.accessKey,
            body=hashlib.md5(body.encode('utf-8')).hexdigest(),
            sign=self.getSignature(body, self.secretKey)
        )

    @staticmethod
    def getSignature(body, secret_key) -> str:
        return hashlib.sha256(f'{body}.{secret_key}'.encode('utf-8')).hexdigest()

    def start_chat(self, crequest: DevChatRequest) -> DevChatResponse:
        json_ = crequest.toJsonString()
        url = f'{self.host}/chat'
        res = requests.post(url, headers=self.getHeaderDict(json_))
        return DevChatResponse(res.content)
