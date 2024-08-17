import streamlit as st
import openpyxl

hide_github_icon = """
<style>
.css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK, 
#MainMenu, footer, header {
  display: none !important;  // Ensures these elements are completely removed from view
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)


import matplotlib.pyplot as plt
from data_utils import load_data, search_by_name, filter_by_gender, people_in_age_range,search_by_names


data = load_data('pidimadugu_records.xlsx')

# Streamlit user interface
st.title('Data Search of the Village')
st.title("paidimadugu")



# Display total voters and gender count
total_voters = len(data)
male_count = len(data[data['Gender'].str.lower() == 'male'])
female_count = len(data[data['Gender'].str.lower() == 'female'])

# Display total voters and gender count
total_voters = len(data)
st.write(f"Total Voters: {total_voters}")
st.write(f"Male: {male_count} and Female: {female_count}")

# Pie chart for gender distribution
fig, ax = plt.subplots()
ax.pie([male_count, female_count], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)

## Name search
st.title('Search for Names')
input_names = st.text_input("Enter name(s), separated by commas for multiple (e.g., kalvakuntala,juvvadi):")
if st.button('Search'):
    results, name_count = search_by_names(data, input_names)
    st.write(results)
    if name_count > 0:
        name_percentage = (name_count / total_voters) * 100
        st.write(f"Number of people with name(s) '{input_names}': {name_count}")
        st.write(f"Percentage of total: {name_percentage:.2f}%")
        
        # Pie chart for name search distribution
        fig, ax = plt.subplots()
        ax.pie([name_count, total_voters - name_count], labels=[input_names, 'Others'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
    else:
        st.write("No results found.")

# Gender filter
st.subheader('Filter by Gender')
gender = st.selectbox('Select Gender:', ['Male', 'Female'], key='gender_select')
if st.button('Filter Gender', key='gender_filter'):
    gender_results = filter_by_gender(data,gender)
    st.write(gender_results)

# Age filter
st.subheader('People within a specified age range')
min_age, max_age = st.slider('Select age range:', 18, 100, (18, 25))
if st.button('Show People Within Age Range', key='age_range'):
    age_results, age_count = people_in_age_range(data, min_age, max_age)
    st.write(age_results)
    if age_count > 0:
        age_percentage = (age_count / total_voters) * 100
        st.write(f"Number of people aged {min_age} to {max_age}: {age_count}")
        st.write(f"Percentage of total: {age_percentage:.2f}%")
        
        # Pie chart for age range distribution
        fig, ax = plt.subplots()
        ax.pie([age_count, total_voters - age_count], labels=[f'{min_age}-{max_age}', 'Others'], autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        st.pyplot(fig)
