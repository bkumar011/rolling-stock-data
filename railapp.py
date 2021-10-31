import pandas as pd
import streamlit as st
import datetime
#from st_aggrid import AgGrid

df=pd.read_csv("railwagon.csv")

st.title("Database of Rolling Stock over Indian Railways")
st.write("_______________________________________________")
st.sidebar.radio("Select the Rolling Stock",('Coaches','Wagons'))

# Select types of wagon to display - User Input
types = df['Type of Stock'].drop_duplicates()
types=types.to_list()
types.insert(0,'All')
type_choice = st.sidebar.selectbox('Select type of stock:', types)

# Remove type of stock from the list of columns
columns=df.columns.to_list()
org_columns=columns.copy()
columns.remove("Type of Stock")
columns.insert(0,'All')

#Select columns to display
options=st.sidebar.multiselect('Select Parameters for display',columns)

#Add Type of Stock column
if 'All' in options:
    disp_col= org_columns
else:
    disp_col=options

#Select columns of data frame to be displayed
#st.write(disp_col)

if len(disp_col) == 0:
    st.write("Choose some parameters to display !!!")

#AgGrid(df)
if type_choice == 'All' :
    
    st.dataframe(df[disp_col],1500,800)
    
else:
    
    disp_df=df.loc[df['Type of Stock']==type_choice]   
    st.dataframe(disp_df[disp_col],1500,800)
    
code= st.sidebar.text_input('Enter code for searching a specific Rolling Stock')
#st.dataframe(df.style.highlight_null(null_color="green"),1500,800)

st.write("The searched wagon code")
if code != '':
    disp_df = df.loc[df['Mech. Code'] == code]
    st.dataframe(disp_df,1500,800)



#st.sidebar.button("CLICK")
#st.table(df)

#st.write(df)