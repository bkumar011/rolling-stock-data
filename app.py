import pandas as pd
import streamlit as st
import datetime
#from st_aggrid import AgGrid

df=pd.read_csv("railwagonv1.csv")

st.title("Database of Rolling Stock over Indian Railways")
st.write("_______________________________________________")
stock = st.sidebar.radio("Select the Rolling Stock",('Coaches','Wagons'))

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
    if 'Mech. Code' not in options:
        disp_col=options
        disp_col.insert(0,'Mech. Code')
    else:
        disp_col=options

#Select columns of data frame to be displayed
#st.write(disp_col)

#if len(disp_col) == 0:
#st.write("Choose some parameters to display !!!")

code= st.sidebar.text_input('Enter code for searching a specific Rolling Stock')


#AgGrid(df)
if type_choice == 'All' and code == '' and stock == 'Wagons':
    
    st.dataframe(df[disp_col],1500,800)
    
elif code == '' and stock == 'Wagons':
    
    disp_df=df.loc[df['Type of Stock']==type_choice]   
    st.dataframe(disp_df[disp_col].transpose(),1500,800)
 
elif stock == 'Wagons':

    disp_df = df.loc[df['Mech. Code'] == code]
    st.table(disp_df.transpose())
    #st.dataframe(disp_df,1500,800)
    # for col in disp_df.columns:

    #     st.write(col,'---->>>',disp_df.iloc[0][col])
    #     st.write('******************')

else:
    st.write("Coaching database is currently under development.. Please check Wagons for the time being !!")

st.sidebar.markdown("Copyright © 2021 Northern Railway")

#st.dataframe(df.style.highlight_null(null_color="green"),1500,800)

##if code != '':
##    disp_df = df.loc[df['Mech. Code'] == code]
##    st.dataframe(disp_df,1500,800)



#st.sidebar.button("CLICK")
#st.table(df)

#st.write(df)