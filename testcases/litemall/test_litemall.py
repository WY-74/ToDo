from pages.litemall.litemall_pages import LitemallPages


class TestLetmall:
    def setup_class(self):
        self.page = LitemallPages(None)
        self.page.login_admin()
        self.page.login_user()

    # 上架商品
    def test_01_add_goods(self):
        self.page.add_goods()

    # 加入购物车
    def test_02_add_cart(self):
        self.page.add_cart()

    # 数据清理-删除商品
    def test_03_delete_goods(self):
        self.page.delete_goods()
