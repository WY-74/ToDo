from dataclasses import dataclass


@dataclass
class AccessToken:
    url: str = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    params = {"corpid": "wwb316419364456d42", "corpsecret": "dD9WmThwalNlSCRuIyWo-PCmorN5HBKOIRM2vwPeFds"}


@dataclass
class Create:
    url: str = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
    json_params = {"name": "WangYun", "parentid": 1, "order": 1}


@dataclass
class GetList:
    url: str = "https://qyapi.weixin.qq.com/cgi-bin/department/simplelist"
