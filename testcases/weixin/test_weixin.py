from pages.weixin.weixin_pages import WeixinPages


class TestWeixin:
    def setup_class(self):
        self.page = WeixinPages(None)
        self.page.get_access_token()

    # 创建部门
    def test_01_create(self):
        self.page.create()

    # 获取列表
    def test_02_get_list(self):
        self.page.get_list()
