from player import Player
from enemy import Enemy
from field import Field
from display import Display
from controller import InputWithoutEnter
import logging
import random
import threading
import time

logger = logging.getLogger(__name__)


class Game:
    """ゲームクラス
    ゲームの初期設定とメインループを実行してゲームを実施するクラス．

    Attributes:
        players (list[Player]): プレイヤーのリスト
        enemies (list[Enemy]): 敵のリスト
        field (Field): フィールドのインスタンス
    """
    def __init__(self) -> None:
        """
        Gameクラスの初期化を行う関数

        """
        self.field = None
        self.players = list[Player]
        self.enemies = list[Enemy]

    def setup(self):
        """
        ゲームのセットアップを行う
        """
        player_num = input("プレイヤー人数：")
        field_size_x = input("フィールドのxサイズ：")
        field_size_y = input("フィールドのyサイズ：")
        field_size_x_int = int(field_size_x)
        field_size_y_int = int(field_size_y)
        enemy_num = random.randint(1, field_size_x_int)
        self.players = []
        self.enemies = []
        for _ in range(int(player_num)):
            self.players.append(
                Player(
                    random.randrange(1, field_size_x_int - 1),
                    random.randrange(1, field_size_y_int - 1)
                    )
                )
        for _ in range(int(enemy_num)):
            self.enemies.append(
                Enemy(
                    random.randrange(1, field_size_x_int - 1),
                    random.randrange(1, field_size_y_int - 1)
                    )
            )
        self.field = Field(
            self.players,
            self.enemies,
            field_size_x_int,
            field_size_y_int
            )

    def update_field(self):
        """
        ディスプレイを更新するループ
        """
        while True:
            display = Display(self.field)
            self.field.generate_map()
            display.update()
            time.sleep(0.01)

    def player_move(self):
        """
        プレイヤー動作ループ
        """
        while True:
            for player in self.field.players:
                player.get_next_pos(InputWithoutEnter.input_without_enter())

    def enemy_move(self):
        """
        敵動作ループ
        """
        while True:
            for enemy in self.field.enemies:
                enemy.get_random_pos()
            time.sleep(1)

    def play(self):
        """
        ゲームを始める
        """
        display_thread = threading.Thread(
            target=self.update_field,
            name='display_thread',
            daemon=True)
        enemy_thread = threading.Thread(
            target=self.enemy_move,
            name='enemy_thread',
            daemon=True)
        player_thread = threading.Thread(
            target=self.player_move,
            name='player_thread',
            daemon=True)

        enemy_thread.start()
        player_thread.start()
        display_thread.start()

        enemy_thread.join()
        player_thread.join()
        display_thread.join()
