import streamlit as st
import re

# def convert_gpt_to_typora_qiita(text):
#     inline_math = re.compile(r'\\\((.*?)\\\)')
#     text = inline_math.sub(r'$\1$', text)
#     block_math = re.compile(r'\\\[(.*?)\\\]')
#     text = block_math.sub(r'$$\1$$', text)
#     return text
#

def convert_gpt_to_typora_qiita(text):
    # 行内の数式を検出して変換
    inline_math = re.compile(r'\\\((.*?)\\\)')
    text = inline_math.sub(r'$\1$', text)

    # ブロックの数式を検出して変換
    # ここでパターンを `\[(.*?)\]` から改善しています。
    block_math = re.compile(r'\\\[([\s\S]*?)\\\]')
    text = block_math.sub(r'$$\1$$', text)

    return text

    return text
st.title("Markdown Converter")

col1, col2 = st.columns(2)

with col1:
    st.header("Original Markdown (ChatGPT)")
    original_text = st.text_area("Paste your Markdown here:", height=300)
    if st.button("Convert"):
        converted_text = convert_gpt_to_typora_qiita(original_text)

with col2:
    st.header("Converted Markdown (Typora/Qiita)")
    if 'converted_text' in locals():
        st.text_area("Converted Markdown:", converted_text, height=300)
        st.markdown(converted_text, unsafe_allow_html=True)

st.caption("Developed by TOMOMI RESEARCH INC.")
