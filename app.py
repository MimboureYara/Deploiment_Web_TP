import streamlit as st
import pandas as pd
import numpy as np

def main():
    st.write("Mon premier pas en streamlit")
    ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
    ser2 = pd.Series(np.arange(26))
    df = pd.DataFrame({"lettre":ser1, "num":ser2}).reset_index()
    st.dataframe(df)
    st.write("Lettres d'alphabet en fonction du numero d'ordre")
    st.line_chart(df.lettre)

if __name__ == '__main__':
    main()