import streamlit as st
import requests
import re
from bs4 import BeautifulSoup
from collections import Counter
import jieba
from pyecharts import options as opts
from pyecharts.charts import WordCloud, Bar, Pie, Line, Scatter, Funnel, Polar

def remove_html_tags(text):
    cleanr = re.compile('<.*?>')
    return re.sub(cleanr, '', text)

def get_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return remove_html_tags(text)

def process_text(text):
    words = jieba.lcut(text)
    words = [word for word in words if len(word) > 1]
    word_counter = Counter(words)
    top_words = word_counter.most_common(20)
    return top_words

def plot_word_cloud(top_words):
    c = WordCloud()
    c.add("", top_words)
    return c

def plot_bar(top_words):
    c = Bar()
    c.add_xaxis([i[0] for i in top_words])
    c.add_yaxis("Frequency", [i[1] for i in top_words])
    return c

def plot_pie(top_words):
    c = Pie()
    c.add("", top_words)
    return c

def plot_line(top_words):
    c = Line()
    c.add_xaxis([i[0] for i in top_words])
    c.add_yaxis("Frequency", [i[1] for i in top_words])
    return c

def plot_scatter(top_words):
    c = Scatter()
    c.add_xaxis([i[0] for i in top_words])
    c.add_yaxis("Frequency", [i[1] for i in top_words])
    return c

def plot_funnel(top_words):
    c = Funnel()
    c.add("", top_words)
    return c

def plot_polar(top_words):
    c = Polar()
    c.add("", top_words, type_='bar')
    return c

def main():
    st.title("Text Analysis with Streamlit")
    url = st.text_input("请输入需要分析的网页 URL")
    if url:
        text = get_text_from_url(url)
        top_words = process_text(text)
        st.header("词云图")
        st_pyecharts(plot_word_cloud(top_words))
        st.header("条形图")
        st_pyecharts(plot_bar(top_words))
        st.header("饼状图")
        st_pyecharts(plot_pie(top_words))
        st.header("线状图")
        st_pyecharts(plot_line(top_words))
        st.header("散点图")
        st_pyecharts(plot_scatter(top_words))
        st.header("漏斗图")
        st_pyecharts(plot_funnel(top_words))
        st.header("极坐标图")
        st_pyecharts(plot_polar(top_words))

def st_pyecharts(chart):
    chart.render("temp_chart.html")
    with open("temp_chart.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    st.components.v1.html(html_code, height=500)

if __name__ == "__main__":
    main()