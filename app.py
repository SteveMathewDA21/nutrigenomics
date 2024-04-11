import pandas as pd
import streamlit as st

df = pd.read_excel('Nut_dep_ob.xlsx')

def process_dataframe(df, string_input, dropdown1, dropdown2):
    temp = df[df['rsiD']==string_input]
    temp = temp[temp['Allelic Variation']==dropdown1]
    temp = temp[temp['Associated Disorder']==dropdown2]
    recommended = ''
    for i in temp['Recommended']:
        recommended=recommended+i+", "
    if recommended == '':
        recommended = '(Not found in the existing dataset)'
    return recommended
def main():
    st.title('Nutrigenomics and Dietary Code')

    string_input = st.text_input('Enter the rsID:')
    dropdown1 = st.selectbox('Select the allelic variation:', df['Allelic Variation'].unique())
    dropdown2 = st.selectbox('Select the associated disorder:', df['Associated Disorder'].unique())

    if st.button('Suggest diet'):
        result = process_dataframe(df, string_input, dropdown1, dropdown2)
        result = "Suggested diet: \n\n"+result
        st.write(result)

if __name__ == '__main__':
    main()
