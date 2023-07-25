from TreasureBox.treasure import BaseRequests
from data.weixin import weixin_data
from data.weixin import weixin_location


class WeixinPages(BaseRequests):
    def __init__(self, driver: None):
        super().__init__(driver)
        self.yaml = "/Users/ya/wangyun/ToDo/assert/weixin.yaml"
        self.data = weixin_data
        self.location = weixin_location

    def get_access_token(self):
        response = self.http_methods("get", self.data.AccessToken.url, params=self.data.AccessToken.params)
        self.assert_by_yamlmap(response, self.yaml)
        self.get_token(response, self.location.AccessToken.get_token, "access_token")

    def create(self):
        response = self.http_methods("post", self.data.Create.url, params=self.token, json=self.data.Create.json_params)
        self.assert_by_yamlmap(response, self.yaml)

    def get_list(self):
        response = self.http_methods("get", self.data.GetList.url, params=self.token)
        self.assert_by_jsonschema(response)
