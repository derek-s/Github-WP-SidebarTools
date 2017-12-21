# !/usr/bin/python
# -*- coding:UTF-* -*-

import json
import codecs
import requests
import arrow


typefile = open('type.json', 'r').read()
otherfile = open('other.json', 'r').read()
jsonfile = codecs.open('day.json', 'w+', encoding="utf-8")

typelist = json.loads(typefile)
otherlist = json.loads(otherfile)
jsonob = []


Url = 'eventsurl' # api.github.com/user/name/events
Req = requests.get(Url)
ReqJSON = Req.json()

for reqa in ReqJSON:
    for typex in typelist:
        if typex['type'] == reqa['type']:
            if reqa['type'] == 'CreateEvent':
                opera = typex['desc']
                for otherx in otherlist:
                    if otherx['ref_type'] == reqa['payload']['ref_type']:
                        operb = otherx['desc']
            else:
                opera = typex['desc']
                operb = ''
    repo_name = reqa['repo']['name']
    create_time = arrow.get(
        reqa['created_at']
        ).to('Asia/Shanghai').format("YYYY-MM-DD HH:mm:ss")
    dynamic = {
        "operation": opera+operb,
        "reponame": repo_name,
        "creattime": create_time
    }
    jsonob.append(dynamic)

json.dump(jsonob, jsonfile, indent=4, ensure_ascii=False)