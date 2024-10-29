import os
from field import Field
from player import Player


class Display:
    """
    Displayクラス
    Displayクラスは、画面にフィールドを表示します。
    """

    def __init__(self) -> None:
        """
        Displayクラスの初期化を行う関数

        """
        pass

    def update(self, field_data: Field) -> None:
        """
        画面表示の更新をする

        Args:
            field_data (Field):フィールドクラス

        Returns:
            None

        Examples:
            >>> pac_field = Field([Player(0,0)],3,3)
            >>> field_map = pac_field.generate_map()
            >>> display = Display()
            >>> display.update(pac_field)
            😶　　
            　　　
            　　　
        """
        os.system("clear")

        field_map = field_data.f_map

        for row in field_map:
            for item in row:
                print(item, end="")
            print()


if __name__ == '__main__':
    import doctest
    doctest.testmod()
