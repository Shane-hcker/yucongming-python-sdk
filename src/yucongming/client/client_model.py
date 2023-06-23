# -*- encoding: utf-8 -*-
import datetime
import hashlib
import requests
from random import sample

from .chat.crequest import *
from .chat.cresponse import *


class YCMClient:
    def __init__(self, accessKey=None, secretKey=None):
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.host: Final = 'https://www.yucongming.com/api/dev'

    def getHeaderDict(self, body) -> Dict[str, str]:
        if not (self.accessKey or self.secretKey):
            raise InterruptedError('access key or secret key hasn\'t been setup yet')
        e_body = hashlib.md5(body.encode('utf-8')).hexdigest()
        date = f"{datetime.datetime.now().timestamp():.0f}"
        return dict(
            accessKey=self.accessKey,
            sign=self.getSignature(e_body, self.secretKey),
            body=e_body,
            nonce=str(sample(range(1, 10), 4)),
            timestamp=date,
        )

    @staticmethod
    def getSignature(body, secret_key) -> str:
        stuff = hashlib.sha256(f'{body}.{secret_key}'.encode('utf-8')).hexdigest()
        return stuff

    def start_chat(self, crequest: DevChatRequest) -> DevChatResponse:
        json_ = crequest.toJsonString()
        url = f'{self.host}/chat'
        headers = self.getHeaderDict(json_)
        # headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        #                               'Chrome/86.0.4240.198 Safari/537.36'})
        print(headers)
        res = requests.post(url, headers=headers)
        return DevChatResponse(res.content)
