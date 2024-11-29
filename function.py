from __future__ import unicode_literals
import whisper
import pathlib
import math
from functools import reduce
# import ssl
# import requests
# ssl._create_default_https_context = ssl._create_unverified_context

# whisperのモデルをロードして音声・動画ファイルを読み込ませる。transcriptの結果を返す
def transcribe(file: str):
    model = whisper.load_model("turbo")
    # model = whisper.load_model("large")
    transcribe_result = model.transcribe(file)
    return transcribe_result["segments"]

# セグメントの音声・動画開始時間がwhisperから秒単位で返されるため、自分秒単位に変換する関数
def convert_time(t: float):
    hour = math.floor(t / (60 * 60))
    minute = math.floor(t / 60) - (hour * 60)
    sec = math.floor(t % 60)
    msec = round((t % 1) * (10**3))

    return f"{hour:02}:{minute:02}:{sec:02}.{msec:03}"

# セグメントから取得した時間情報とテキスト情報を、ファイルにインプとするフォーマット変換する関数
def get_srt_section(index: int, start_sec: float, end_sec: float, text: str):
    start = convert_time(start_sec)
    end = convert_time(end_sec)
    return [
        f"{index}",
        f"{start} --> {end}",
        text,
        ""
    ]

# 結果をテキストファイルに書き込む
def write_file(file_name: str, text: str):
    with open(file_name, "w") as f:
        f.write(text)

# ファイルのpath情報を取得する？
def get_file_stem(file_name: str):
    return pathlib.PurePath(file_name).stem