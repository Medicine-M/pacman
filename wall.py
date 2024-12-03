from item import Item


class Wall(Item):
    """ウォールクラス
    Itemを継承して作成したウォールクラス.
    wallのアイコンを更新するメソッドを追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(self, x, y) -> None:
        """
        wallの初期化
        """
        super().__init__(x, y)
        self.icon = "🔲"


if __name__ == "__main__":
    import doctest
    doctest.testmod()
