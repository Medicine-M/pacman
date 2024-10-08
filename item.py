"""親クラス
block,player,enemy,cookieの親クラス
"""


class Item:
    """block,player,enemy,cookieの親クラス

    Attributes:
       now_x(int) : 現在のx座標
       now_y(int) : 現在のy座標
       next_x(int) : 次の時刻でのx座標
       next_y(int) : 次の時刻でのy座標
       icon(str) : 表示されるアイテムのアイコン
    """

    def __init__(x, y) -> None:
        pass