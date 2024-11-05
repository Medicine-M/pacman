from player import Player
from field import Field
from display import Display
from controller import InputWithoutEnter
import logging
import random

logger = logging.getLogger(__name__)


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        field (Field): フィールドのインスタンス
    """
    def __init__(self) -> None:
        """
        Gameクラスの初期化を行う関数

        """
        self.field = None
        self.players = list[Player]

    def setup(self):
        """
        ゲームのセットアップを行う
        """
        player_num = input("プレイヤー人数：")
        field_size_x = input("フィールドのxサイズ：")
        field_size_y = input("フィールドのyサイズ：")
        field_size_x_int = int(field_size_x)
        field_size_y_int = int(field_size_y)
        self.players = []
        for _ in player_num:
            self.players.append(
                Player(
                    random.randrange(0, field_size_x_int - 1),
                    random.randrange(0, field_size_y_int - 1)
                    )
                )
        self.field = Field(self.players, field_size_x_int, field_size_y_int)

    def play(self):
        """
        ゲームを始める
        """
        while True:
            display = Display(self.field)
            self.field.generate_map()
            display.update()
            for player in self.field.players:
                player.get_next_pos(InputWithoutEnter.input_without_enter())
