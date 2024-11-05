import os
from field import Field


class Display:
    """
    Displayクラス
    Displayクラスは、画面にフィールドを表示します。
    """

    def __init__(self, field_data: Field) -> None:
        """
        Displayクラスの初期化を行う関数

        """
        self.field_data = field_data

    def update(self) -> None:
        """
        画面表示の更新をする

        Args:
            field_data (Field):フィールドクラス

        Returns:
            None

        Examples:
            >>> from player import Player
            >>> pac_field = Field([Player(0,0)],3,3)
            >>> field_map = pac_field.generate_map()
            >>> display = Display(pac_field)
            >>> display.update()
            😶　　
            　　　
            　　　
        """
        os.system("clear")

        field_map = self.field_data.f_map

        for row in field_map:
            for item in row:
                print(item, end="")
            print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
