import streamlit as st
import datetime
from calculate import calculate_end_date

st.title(" Classroom Calculator")

start_date = st.date_input("Start Date", format="DD/MM/YYYY")

end_old_programme_date = st.date_input("End Old Programme Date", format="DD/MM/YYYY")

holidays = st.number_input("Holidays Taken Old Programme", min_value=0, max_value=40)

if st.button("Calculate"):
    new_date, days_performed, days_performed_old = calculate_end_date(start_date=start_date, end_date_old_programme=end_old_programme_date, holiday_old=holidays)
    new_date = new_date.strftime("%d/%m/%Y")
    st.write(f"Days Performed Old Programme: {days_performed_old}")
    st.write(f"Days To Perform New Programme: {days_performed}")
    st.write(f"New Date To Complete: {new_date}")
    
    


