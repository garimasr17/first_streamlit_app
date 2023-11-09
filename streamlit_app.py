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

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
