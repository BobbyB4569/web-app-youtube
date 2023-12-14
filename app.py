# Imports
import streamlit as st 
import pandas as pd 
import seaborn as sns

# 1. Title and Subheader
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

# 2. Upload Dataset
upload = st.file_uploader("Upload your dataset (in CSV format)")
if upload is not None:
    data=pd.read_csv(upload)

# 3. Show dataset
if upload is not None:
    if st.checkbox("Preview dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

# 4. Check datatype of each column
if upload is not None:
    if st.checkbox("datatype of each column"):
        st.text("Datatypes")
        st.write(data.dtypes)

# 5. Find shape of dataset (number of rows and columns)
if upload is not None:
    data_shape=st.radio("What dimension would you like to check?",('Rows','Columns'))

    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0]) 
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])    

# Remove deprecation warning associated with Streamlit pyplot
st.set_option('deprecation.showPyplotGlobalUse', False)
# 6. Find Null values in the dataset
if upload is not None:
    test=data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congrats, No missing values")
        

# 7. Find Duplicate values in the dataset
if upload is not None:
    test=data.duplicated().any()
    if test==True:
        st.warning("This dataset is shit and contains duplicate values")
        dup=st.selectbox("Do you want to remove duplicate values?", \
                         ("Select one","Yes","No"))  
        if dup=="Yes":
            data = data.drop_duplicates()  
            st.text("Duplicate values removed")
        if dup=="No":
            st.text("OK, go fuck yourself")


# 8. Get overall statistics
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include='all'))       

# 9. About section
        
if st.button("About App"):
    st.text("Built with Streamlit using Python in VS code")
    st.text("Bobby is the shit!")

# 10. By
if st.checkbox("By"):
    st.success("Bobby Bankert")
