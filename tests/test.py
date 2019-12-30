# -*- coding: utf-8 -*-

from opentracing_flask import *


resp = g_requests.get("http://www.baidu.com")
print(resp.text)