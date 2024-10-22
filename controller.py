class Controller:
    """
    Controllerクラス
    プレイヤーからの入力を管理するクラスです。
    """

    def __init__(self) -> None:
        """
        Controllerクラスの初期化を行う関数

        Args:
            なし
        """
        pass

    def wait_input(self) -> int:
        """
        キーボードからの入力を待ち、入力を数値として返す関数です。

        Returns:
            int: 0:上 1:右 2:下 3:左

        Examples:
            >>> controller = Controller()
            >>> p = controller.wait_input()
            1
            >>> print(p)
            1

        """
        pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()
