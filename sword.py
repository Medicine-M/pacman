from item import Item


class Sword(Item):
    """ソードクラス
    Itemを継承して作成したソードクラス.
    入力から移動方向を受け取って移動しようとする方向を計算するメソッドと
    マップから移動して良いと許可が出た時に呼び出される座標を更新するメソッド
    を追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
    """

    def __init__(self, x, y) -> None:
        """
        swordの初期化
        """
        super().__init__(x, y)
        self.icon = "🗡️"
        self.status = True

    def toggle_status(self):
        """
        swordがplayerと衝突したときswordのアイコンを消す
        """
        self.status = False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
