import streamlit as st
import function as f
from pydub import AudioSegment
from pydub.playback import play
import os

# os.system('git clone https://git.ffmpeg.org/ffmpeg.git ffmpeg')
# os.system('sudo apt update')
# os.system('sudo apt install ffmpeg')


def main_function(FILE_NAME: str):
    movie_segments = f.transcribe(FILE_NAME)

    # source_srt_list: list[str] = f.reduce(
    #     lambda arr, curr: arr + f.get_srt_section(
    #         curr[0],
    #         curr[1]["start"],
    #         curr[1]["end"],
    #         curr[1]["text"]),
    #     enumerate(movie_segments),
    #     [])
    # f.write_file(f"{f.get_file_stem(FILE_NAME)}.srt", "\n".join(source_srt_list))

    movie_texts = [seg["text"] for seg in movie_segments]
    f.write_file(f"{f.get_file_stem(FILE_NAME)}.txt", "\n".join(movie_texts))
    return f"{f.get_file_stem(FILE_NAME)}.txt"
    
st.title("MP3/M4Aファイルの音声を文字起こし")  # ② タイトル表示

# ファイルの読み込み
st.subheader("1.MP3/M4Aファイルをアップロードしてください。")
uploaded_file = st.file_uploader("MP3/MP4ファイル", type=['mp3', 'm4a'] )
st.audio(uploaded_file, format="audio/mpeg", loop=True)
# print(uploaded_file)
# if uploaded_file is not None :
#     audio_data = AudioSegment.from_file(uploaded_file)
    # audio_data.export("output.mp3", format="mp3")
    # FILE_NAME = 'output.mp3'

    # transcript_result_file_name = main_function(FILE_NAME)
    # print(transcript_result_file_name)
    # with open(transcript_result_file_name, "r") as f:
    #     txt = f.read()
    #     st.download_button(
    #     label="Download .txt file",
    #     data=txt,
    #     file_name="result.txt",
    #     mime="text/csv",
    #     )
