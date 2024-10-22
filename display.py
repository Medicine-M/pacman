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

    def update(self, field_data: dict[str, list[Player]]) -> None:
        """
        画面表示の更新をする

        Returns:
            None

        Examples:
            >>> field = Display()
            >>> field.update()
            >>> ""
        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
