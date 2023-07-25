from TreasureBox.treasure import BaseRequests
from data.litemall.litemall_location import LitemallLocation
from data.litemall.litemall_data import LitemallURL, Litemall


class LitemallPages(BaseRequests):
    def __init__(self, driver: None):
        super().__init__(driver)
        self.url = LitemallURL
        self.data = Litemall
        self.location = LitemallLocation
        self.yamlpath = "/Users/ya/wangyun/ToDo/assert/litemall/add_goods.yaml"

    def login_admin(self):
        r = self.http_methods("post", self.url.login_admin, json=self.data.admin, verify=False)
        self.get_token(r, self.location.TOKEN, "admin")

    def login_user(self):
        r = self.http_methods("post", self.url.login_user, json=self.data.user, verify=False)
        self.get_token(r, self.location.TOKEN, "user")

    def add_goods(self):
        r = self.http_methods(
            "post",
            self.url.add_goods,
            headers={"X-Litemall-Admin-Token": self.token["admin"]},
            json=self.data.add_goods,
            verify=False,
        )
        self.assert_status_code(r)
        self.assert_by_yamlmap(r, self.yamlpath)

    def add_cart(self):
        self.goodsid, productid = self.get_goodsid_and_productid()
        json_params = {"goodsId": self.goodsid, "number": 1, "productId": productid}
        response = self.http_methods(
            "post", self.url.add_cart, headers={"X-Litemall-Token": self.token["user"]}, json=json_params, verify=False
        )
        self.assert_by_yamlmap(response, self.yamlpath)

    def get_goodsid_and_productid(self):
        response1 = self.http_methods(
            "get",
            self.url.goods_list,
            headers={"X-Litemall-Admin-Token": self.token["admin"]},
            params={"limit": 10, "name": "WangYun", "order": "desc", "page": 1, "sort": "add_time"},
            verify=False,
        )
        goodsid = self.get_text_from_root(response1, self.location.GOODSID)
        resopnse2 = self.http_methods(
            "get",
            self.url.goods_detail,
            headers={"X-Litemall-Admin-Token": self.token["admin"]},
            params={"id": goodsid},
            verify=False,
        )
        productid = self.get_text_from_root(resopnse2, self.location.PRODUCTID)
        return goodsid, productid

    def delete_goods(self):
        response = self.http_methods(
            "post",
            self.url.delete_goods,
            headers={"X-Litemall-Admin-Token": self.token["admin"]},
            json={"id": self.goodsid},
            verify=False,
        )
        self.assert_by_yamlmap(response, self.yamlpath)
