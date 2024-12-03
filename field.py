from player import Player
from enemy import Enemy


class Field:
    """
    Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新しフィールドの配列を生成します。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        f_size_x (int): x方向フィールドサイズ
        f_size_y (int): y方向フィールドサイズ
        f_map (list(list(str))): フィールドマップ
        items (dict[str, list(Item)]): フィールド内のItemすべてのリスト
    """
    def __init__(self,
                 players: list[Player],
                 enemies: list[Enemy],
                 f_size_x: int,
                 f_size_y: int,
                 ) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
            enemies (list[Enemy]): 敵のリスト
            items (dict[str, list(Item)]): フィールド内のItemすべてのリスト
            f_size_x (int): x方向フィールドサイズ
            f_size_y (int): y方向フィールドサイズ
        """
        self.players = players
        self.enemies = enemies
        self.f_size_x = f_size_x
        self.f_size_y = f_size_y
        self.f_map = [["　" for _ in range(f_size_x)] for _ in range(f_size_y)]
        self.items = dict()
        self.items["players"] = players
        self.items["enemies"] = enemies

    def generate_map(self) -> list[list[str]]:
        """
        プレイヤーの新しい情報からその時点でのマップを生成する。

        Returns:
            list[list[str]]: {マップ情報のリスト}

        Examples:
            >>> pac_field = Field([Player(1,1)],[Enemy(0,0)],5,5)
            >>> field_map = pac_field.generate_map()
            >>> print(field_map[1][1])
            😶
        """
        prev_map = self.f_map
        self.f_map = [
                    ["　" for _ in range(self.f_size_x)]
                    for _ in range(self.f_size_y)
                ]
        for items in self.items:
            for item in self.items[items]:
                if (item.next_x >= self.f_size_x
                        or item.next_x < 0
                        or item.next_y >= self.f_size_y
                        or item.next_y < 0):
                    item.update_pos(True)
                else:
                    if (item.icon == self.players[0].icon):
                        if (prev_map[item.next_y][item.next_x] == self.enemies[0].icon):
                            item.update_pos()
                            item.toggle_status()
                    item.update_pos()
                self.f_map[item.now_y][item.now_x] = item.icon

        return self.f_map


if __name__ == '__main__':
    import doctest
    doctest.testmod()
