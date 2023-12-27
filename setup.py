from setuptools import setup, find_packages

setup(
    name='bz',  # 项目名称
    version='0.1.0',  # 项目版本
    url='https://github.com/yc-eng/streamlit',  # 项目的URL
    author='yc-end',  # 作者名字
    author_email='2366244813@qq.com',  # 作者邮箱
    description='nbclass',  # 项目简介
    packages=find_packages(),  # 自动发现所有包和子包
    install_requires=[  # 项目依赖
        'streamlit',
        'Requests',
        'beautifulsoup4',
        'plotly',
        'jieba',
        'pandas',
        'wordcloud',
        'matplotlib',
        'pyecharts'
    ],
)