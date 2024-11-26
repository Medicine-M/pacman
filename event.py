from field import Field


class Event:
    """
    Eventクラス
    クリア判定などのイベントを司るクラス

    Attributes:
        clear_flag (bool): ゲームのクリアフラグ
        miss_flag (bool): ゲームの失敗フラグ
        exit_flag (bool): ゲーム終了フラグ
        field_data (Field): フィールドのインスタンス
    """

    def __init__(self, field_data: Field) -> None:
        """
        Eventクラスの初期化

        Args:
            field_data (Field): フィールドのインスタンス
        """
        self.field_data = field_data
        self.clear_flag = False
        self.miss_flag = False
        self.exit_flag = False

    def check_clear(self):
        """
        クリア条件を判定し、クリアフラグをTrueにし、ゲーム終了
        
        Examples:
            >>> from player import Player
            >>> from enemy import Enemy
            >>> pac_field = Field([Player(0,0)],[],3,3)
            >>> field_map = pac_field.generate_map()
            >>> event = Event(pac_field)
            >>> event.check_clear()
            >>> print(event.clear_flag)
            True
        """

        if (len(self.field_data.enemies) == 0):
            self.clear_flag = True
            self.exit_flag = True

    def check_miss(self):
        """
        失敗条件を判定し、ゲーム失敗フラグをTrueにし、ゲーム終了

        Examples:
            >>> from player import Player
            >>> from enemy import Enemy
            >>> pac_field = Field([Player(0,0)],[],3,3)
            >>> field_map = pac_field.generate_map()
            >>> event = Event(pac_field)
            >>> pac_field.players[0].toggle_status()
            >>> event.check_miss()
            >>> print(event.miss_flag)
            True
        """
        for player in self.field_data.players:
            if (player.status is False):
                self.miss_flag = True
                self.exit_flag = True

    # def check_overlap(
    #         self, 
    #         now_position: tuple[int, int],
    #         next_position: tuple[int, int]
    #         ) -> tuple[int, int]:
    #     """
    #     アイテムが移動しようとしたとき、その座標で衝突があるか否かを判定します。
    #     また、フィールドの端に来たら対応する数字を返します。

    #     Args:
    #         now_position (tuple[int, int]): 今の座標(int x, int y)
    #         next_position (tuple[int, int]): 移動したい座標(int x, int y)

    #     Examples:
    #         >>> from player import Player
    #         >>> pac_field = Field([Player(0,0)],3,3)
    #         >>> field_map = pac_field.generate_map()
    #         >>> event = Event(pac_field)
    #         >>> print(event.check_overlap((2, 2),(2, 3)))
    #         (2, 0)
    #     """
    #     return_position_x = next_position[0]
    #     return_position_y = next_position[1]
    #     if (next_position[0] >= self.field_data.f_size_x):
    #         return_position_x = 0
    #     if (next_position[1] >= self.field_data.f_size_y):
    #         return_position_y = 0
    #     if (next_position[0] < 0):
    #         return_position_x = self.field_data.f_size_x - 1
    #     if (next_position[1] < 0):
    #         return_position_y = self.field_data.f_size_y - 1

    #     return (return_position_x, return_position_y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
