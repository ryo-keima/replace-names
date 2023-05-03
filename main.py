import datetime

import pandas as pd
from faker import Faker

#### 適宜変更 ####
CSV_FILE = "test.csv"
CSV_FILE_MOD = f"modified_csv_file{datetime.datetime.now()}.csv"
COLUMN_NAME = "name"
################

# CSVファイルを読み込む
df = pd.read_csv(CSV_FILE)

# Fakerインスタンスの作成
fake = Faker("ja_JP")  # 日本語の架空の人物名を生成するためのインスタンス

# 各名前に対応する架空の人物名を生成する辞書を作成
unique_names = df[COLUMN_NAME].unique()  # CSVファイルのnameカラムの値を架空の人物名に変換
name_mapping = {name: fake.name() for name in unique_names}

# nameカラムの値を架空の人物名に置換
df[COLUMN_NAME] = df[COLUMN_NAME].map(name_mapping)

# 書き換えたデータを新しいCSVファイルに保存
output_csv_file = CSV_FILE_MOD
df.to_csv(output_csv_file, index=False)
