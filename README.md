# 鱼聪明SDK For Python

**给程序员鱼皮的网站[鱼聪明](https://yucongming.com)的SDK, 参照了他的鱼聪明Java SDK**



## QuickStart

#### Prerequisites

​	[鱼聪明AI助手配置点此处。](https://github.com/liyupi/yucongming-java-sdk)

---

```python
from yucongming.client import *

client = YCMClient(accessKey, secretKey)
```

配置请求:

```python
request = DevChatRequest()
request.model_id = 1145141919810
request.message = '一个一个一个一个'
```

发送请求并获取返回结果;

```python
chat_res = client.start_chat(request)
print(chat.content)
```

