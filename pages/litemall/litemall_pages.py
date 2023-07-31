from TreasureBox.treasure import BaseRequests
from data.litemall.litemall_location import LitemallLocation
from data.litemall.litemall_data import LitemallURL, Litemall


class LitemallPages(BaseRequests):
    def __init__(self, driver: None):
        super().__init__(driver)
        self.url = LitemallURL
        self.data = Litemall
        self.location = LitemallLocation
        self.yamlpath = "/Users/ya/wangyun/ToDo/mapper/litemall.yaml"

    def __login_admin(self):
        r = self.http_methods("post", self.url.login_admin, json=self.data.admin, verify=False)
        return self.get_token(r, self.location.TOKEN)

    def __login_user(self):
        r = self.http_methods("post", self.url.login_user, json=self.data.user, verify=False)
        return self.get_token(r, self.location.TOKEN)

    def __get_goodsid_and_productid(self):
        response1 = self.http_methods(
            "get",
            self.url.goods_list,
            headers=self.token_group["admin"],
            params=self.data.goods_ids_params,
            verify=False,
        )
        goodsid = self.get_text_from_root(response1, self.location.GOODSID)
        resopnse2 = self.http_methods(
            "get",
            self.url.goods_detail,
            headers=self.token_group["admin"],
            params={"id": goodsid},
            verify=False,
        )
        productid = self.get_text_from_root(resopnse2, self.location.PRODUCTID)
        return goodsid, productid

    def building_token_group(self):
        self.token_group = {}
        self.token_group["admin"] = {"X-Litemall-Admin-Token": self.__login_admin()}
        self.token_group["user"] = {"X-Litemall-Token": self.__login_user()}

    def add_goods(self):
        r = self.http_methods(
            "post",
            self.url.add_goods,
            headers=self.token_group["admin"],
            json=self.data.add_goods,
            verify=False,
        )
        self.assert_status_code(r)
        self.assert_by_yamlmap(r, self.yamlpath)

    def add_cart(self):
        self.goodsid, productid = self.__get_goodsid_and_productid()
        json_params = {"goodsId": self.goodsid, "number": 1, "productId": productid}
        response = self.http_methods(
            "post", self.url.add_cart, headers=self.token_group["user"], json=json_params, verify=False
        )
        self.assert_by_yamlmap(response, self.yamlpath)

    def delete_goods(self):
        response = self.http_methods(
            "post",
            self.url.delete_goods,
            headers=self.token_group["admin"],
            json={"id": self.goodsid},
            verify=False,
        )
        self.assert_by_yamlmap(response, self.yamlpath)
