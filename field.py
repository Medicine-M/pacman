from player import Player


class Field:
    """Fieldクラス
    Fieldクラスは、ゲームのフィールドを表すクラスです。
    プレイヤー、敵、アイテムの位置を更新し、Fieldを表示する機能を持ちます。
    位置を更新する際に衝突判定を行います。

    Attributes:
        players (list[Player]): プレイヤーのリスト
    """
    def __init__(self,
                 players: list[Player],
                 ) -> None:
        pass
