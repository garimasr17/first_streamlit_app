import streamlit

streamlit.title('My Parents new healthy dinner')

streamlit.header('Menu 🥣 🥗 🐔 🥑🍞')

streamlit.text('Scrambelled eggs')
streamlit.text('Puri Bhaji')
streamlit.text('Aloo Paratha')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

