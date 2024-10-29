from player import Player


class Field:
    """
    Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新しフィールドの配列を生成します。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        f_size_x (int): x方向フィールドサイズ
        f_size_y (int): y方向フィールドサイズ
        f_map (list(list(str))): フィールドマップ
        items (dict[str,Player]): フィールド内要素
    """
    def __init__(self,
                 players: list[Player],
                 f_size_x: int,
                 f_size_y: int,
                 ) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
            items (dict[str, Player]): アイテム全体のリスト
            f_size_x (int): x方向フィールドサイズ
            f_size_y (int): y方向フィールドサイズ
        """
        self.players = players
        self.f_size_x = f_size_x
        self.f_size_y = f_size_y
        self.f_map = [["　" for _ in range(f_size_x)] for _ in range(f_size_y)]
        self.items = dict()
        self.items["players"] = players

    def generate_map(self) -> list[list[str]]:
        """
        プレイヤーの新しい情報からその時点でのマップを生成する。

        Returns:
            list[list[str]]: {アイテム種類 : アイテム情報のリスト}

        Examples:
            >>> pac_field = Field([Player(1,1)],5,5)
            >>> field_map = pac_field.generate_map()
            >>> print(field_map[1][1])
            😶
        """

        for items in self.items:
            for item in self.items[items]:
                self.f_map[item.now_y][item.now_x] = item.icon
        return self.f_map


if __name__ == '__main__':
    import doctest
    doctest.testmod()
