# -*- encoding: utf-8 -*-
from random import randrange
import ssl
import datetime
import hashlib

import urllib.request as urequests
import urllib.parse as uparse

from .chat.crequest import *
from .chat.cresponse import *


class YCMClient:
    def __init__(self, accessKey=None, secretKey=None):
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.host: Final = 'https://www.yucongming.com/api/dev'

    def get_data(self, body) -> Dict[str, str]:
        if not (self.accessKey or self.secretKey):
            raise InterruptedError('access key or secret key hasn\'t been setup yet')

        return dict(
            accessKey=self.accessKey,
            body=(encoded_body := hashlib.md5(body.encode('utf-8')).hexdigest()),
            sign=self.getSignature(encoded_body, self.secretKey),
            nonce=str(randrange(1000, 9999)),
            timestamp=f"{datetime.datetime.now().timestamp():.0f}",
        )

    @staticmethod
    def getSignature(body, secret_key) -> str:
        stuff = hashlib.sha256(f'{body}.{secret_key}'.encode('utf-8')).hexdigest()
        return stuff

    def start_chat(self, crequest: DevChatRequest) -> DevChatResponse:
        url = f'{self.host}/chat'
        json_ = crequest.toJsonString()
        data = self.get_data(json_)
        parsed_data = uparse.urlencode(data, encoding='utf-8').encode('utf-8')

        headers = {'Content-Type': 'application/json'}

        context = ssl._create_unverified_context()
        # fixme --> 500 Systematic Error
        request = urequests.Request(url, parsed_data, headers, method='POST')
        res = urequests.urlopen(request, context=context)

        return res.read()
