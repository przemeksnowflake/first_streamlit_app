import streamlit
import pandas as pd

streamlit.title('Something')
streamlit.text('text something')
streamlit.text('🥣 🥗 🐔 🥑🍞 some emojis yo')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
picked_indexes = streamlit.multiselect("Pick some fruits: ", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.iloc[picked_indexes]
streamlit.dataframe(fruits_to_show)
