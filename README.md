# Pacman Project
パックマンに似たゲームを実行する

## Requirement
- Python 3.12

## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- メインプログラムを実行．
  - `result/[日付][実行時刻]/` 下に実行結果とログが出力されます．
```shell
python main.py
```

- 詳しいコマンドの使い方は以下のように確認できます．
```shell
python main.py -h
```


## Parameter Settings

- 指定できるパラメータは以下の通り．半角数字で整数を入力してください.
```shell
プレイヤー人数
フィールドのxサイズ      #フィールドの横の大きさ
フィールドのyサイズ      #フィールドの縦の大きさ
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── README.md           
├── config.py           # パラメータ定義
├── controller.py       # 入力を受け取るファイル
├── display.py          # 画面にフィールドを表示するファイル
├── enemy.py            # エネミークラスのファイル
├── field.py            # ある時点でのフィールドを生成するファイル
├── game.py             # ゲームを実施するファイル
├── item.py             # オブジェクトの親クラスのファイル
├── main.py             # 実行ファイル
├── player.py           # プレイヤークラスのファイル
├── requirements.txt    
├── result              # 結果出力ディレクトリ
└── utils.py            # 共有関数群
```
