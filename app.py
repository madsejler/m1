import streamlit as st

# st.write("Hello")
# st.title("App title")
# st.header("Header")
# st.markdown("Markdown")
# st.subheader("Subheader")
# st.caption("Caption")
# st.code("Code")
# st.latex("Latex")

# import altair as alt
# import numpy as np
# import pandas as pd

# # Compute x^2 + y^2 across a 2D grid
# x, y = np.meshgrid(range(-5, 5), range(-5, 5))
# z = x ** 2 + y ** 2

# # Convert this grid to columnar data expected by Altair
# source = pd.DataFrame({'x': x.ravel(),
#                      'y': y.ravel(),
#                      'z': z.ravel()})

# c1 = alt.Chart(source).mark_rect().encode(
#     x='x:O',
#     y='y:O',
#     color='z:Q'
# )
# st.altair_chart(c1,use_container_width=True)

sentences1 = st.text_input('Name:')
sentences2 = st.text_input('Age:')

if st.button('Submit'):
    st.write('Name:',sentences1)
    st.write('Age:',sentences2)