# -*- coding: utf-8 -*-

from opentracing_flask import *


resp = g_requests.request(method="POST", url="http://www.baidu.com")
print(resp.text)