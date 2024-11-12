from field import Field


class Event:
    """
    Eventクラス
    衝突判定、クリア判定などのイベントを司るクラスです。

    Attributes:
        field_data (Field): フィールドのインスタンス
    """

    def __init__(self, field_data: Field) -> None:
        """
        Eventクラスの初期化

        Args:
            field_data (Field): フィールドのインスタンス
        """
        self.field_data = field_data

    def check_overlap(
            self, 
            now_position: tuple[int, int], 
            next_position: tuple[int, int]
            ) -> tuple[int, int]:
        """
        アイテムが移動しようとしたとき、その座標で衝突があるか否かを判定します。
        衝突があれば現在の座標を返し、
        衝突がなければ次の座標を返します。
        また、フィールドの端以上に移動しようとしたら反対側の座標を返します。

        Args:
            now_position (tuple[int, int]): 今の座標(int x, int y)
            next_position (tuple[int, int]): 移動したい座標(int x, int y)

        Examples:
            >>> from player import Player
            >>> pac_field = Field([Player(0,0)],3,3)
            >>> field_map = pac_field.generate_map()
            >>> event = Event(pac_field)
            >>> print(event.check_overlap((2, 2),(2, 3)))
            (2, 0)
        """
        return_position_x = next_position[0]
        return_position_y = next_position[1]
        if (next_position[0] >= self.field_data.f_size_x):
            return_position_x = 0
        if (next_position[1] >= self.field_data.f_size_y):
            return_position_y = 0
        if (next_position[0] < 0):
            return_position_x = self.field_data.f_size_x - 1
        if (next_position[1] < 0):
            return_position_y = self.field_data.f_size_y - 1

        return (return_position_x, return_position_y)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
