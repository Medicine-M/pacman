from player import Player


class Field:
    """
    Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新しフィールドの配列を生成します。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
    """
    def __init__(self,
                 players: list[Player],
                 ) -> None:
        """
        Fieldクラスの初期化を行う関数

        Args:
            players (list[Player]): プレイヤーのリスト
        """
        self.players = players
        pass

    def update(self) -> dict[str, list[Player]]:
        """
        プレイヤーの新しい情報を受け取りその時点でのマップを生成する。

        Returns:
            dict[str, list[Player]]: {アイテム種類 : アイテム情報のリスト}

        Examples:
            >>>pac_field = Field(Players[20,20])
            >>>field_map = pac_field.update()
            >>>print(field_map.players[0].now_x)
            >>>20
        """
        field_map = {"player": self.players}
        return field_map


if __name__ == '__main__':
    import doctest
    doctest.testmod()
