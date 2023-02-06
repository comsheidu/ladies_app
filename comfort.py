import streamlit as st

x = st.number_input("input first number", step =10)
y = st.number_input("input second number", step =10)


col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.sidebar.button("Add"):
        st.write(x+y)
        
with col2:
    if st.sidebar.button("Subtraction"):
        st.write(x-y)
        
with col3:
    if st.sidebar.button("Multiplication"):
        st.write(x*y)
        
with col4:
    if st.sidebar.button("Division"):
        st.write(x/y)


       
    