# replace-names

CSV ファイルにある個人名を架空の人物の名前に変換するプログラム

## 実行手順

1. ライブラリをインストール

   ```
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. CSV ファイルをカレントディレクトリに配置
3. main.py の以下の値を変更

   - CSV_FILE: 読み込むファイル
   - CSV_FILE_MOD: 出力ファイル名
   - COLUMN_NAME: 名前列のカラム名
