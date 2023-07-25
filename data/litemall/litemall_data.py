from dataclasses import dataclass
from typing import Dict


@dataclass
class LitemallURL:
    baseurl: str = "https://litemall.hogwarts.ceshiren.com/"

    login_admin: str = f"{baseurl}admin/auth/login"
    add_goods: str = f"{baseurl}admin/goods/create"
    goods_list: str = f"{baseurl}admin/goods/list"
    goods_detail: str = f"{baseurl}/admin/goods/detail"
    delete_goods: str = f"{baseurl}admin/goods/delete"

    login_user: str = f"{baseurl}wx/auth/login"
    add_cart: str = f"{baseurl}wx/cart/add"


@dataclass
class Litemall:
    admin = {"username": "hogwarts", "password": "test12345", "code": ""}
    user = {"username": "user123", "password": "user123"}
    add_goods = {
        "goods": {
            "picUrl": "",
            "gallery": [],
            "isHot": False,
            "isNew": True,
            "isOnSale": True,
            "goodsSn": "230722",
            "name": "WangYun",
        },
        "specifications": [{"specification": "规格", "value": "标准", "picUrl": ""}],
        "products": [{"id": 0, "specifications": ["标准"], "price": "100", "number": "100", "url": ""}],
        "attributes": [],
    }
    add_cart = {"goodsId": 1439838, "number": 1, "productId": 259085}
