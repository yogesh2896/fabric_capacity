# import streamlit as st
# import mysql.connector
# from mysql.connector import Error

# # Set page configuration
# st.set_page_config(page_title="Dynamic Fabric Capacity Management", layout="wide")

# # Function to insert data into MySQL
# def insert_data_to_db(data):
#     try:
#         # Establish MySQL connection
#         connection = mysql.connector.connect(
#             host="demodb.cvio4iq4uq97.ap-southeast-2.rds.amazonaws.com",        
#             user="admin",   
#             password="Admin123",
#             database="demo"   
#         )

#         if connection.is_connected():
#             cursor = connection.cursor()
#             # SQL query to insert data
#             for entry in data:
#                 query = """
#                 INSERT INTO fabric_capacity (start_time, end_time, capacity)
#                 VALUES (%s, %s, %s)
#                 """
#                 cursor.execute(query, (entry["Start Time"], entry["End Time"], entry["Capacity"]))
#             connection.commit()
#             return " "
#     except Error as e:
#         return f"Error connecting to MySQL: {str(e)}"
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# # Custom CSS for button and title styling
# st.markdown(
#     """
#     <style>
#     .button-style {
#         background-color: #55b6f9;
#         color: white;
#         font-size: 16px;
#         border: none;
#         border-radius: 5px;
#         padding: 10px 2px;
#         cursor: pointer;
#     }
#     .button-style:hover {
#         background-color: darkorange;
#     }
#     .title-style {
#         background-color: #ff7628;
#         color: white;
#         font-size: 28px;
#         font-weight: bold;
#         text-align: center;
#         padding: 10px 0;
#         border-radius: 8px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Display logo and title
# # Display logo and title
# cols = st.columns([2, 8, 2])  # Adjust widths for equal spacing
# with cols[0]:
#     st.image("https://bgimg6384.s3.us-east-2.amazonaws.com/enoahlogo.png", width=150)  # Replace with your left logo
# with cols[1]:
#     st.markdown('<div class="title-style">Dynamic Fabric Capacity Management</div>', unsafe_allow_html=True)
# with cols[2]:
#     st.image("https://bgimg6384.s3.us-east-2.amazonaws.com/fabriclogo.png", width=80)  # Replace with your right logo
#   # Replace with your right logo

# st.write("")  # Add spacing

# # Create three rows for Start Time, End Time, and Capacity
# data = []
# for i in range(3):
#     cols = st.columns([2, 2, 2])  # Define column widths
#     with cols[0]:
#         start_time = st.time_input(f"Start Time {i+1}", key=f"start_time_{i+1}")
#     with cols[1]:
#         end_time = st.time_input(f"End Time {i+1}", key=f"end_time_{i+1}")
#     with cols[2]:
#         capacity = st.selectbox(f"Fabric Capacity {i+1}", options=["F2", "F4", "F6"], key=f"capacity_{i+1}")
#     data.append({"Start Time": str(start_time), "End Time": str(end_time), "Capacity": capacity})

# st.write("")  # Add spacing

# # Create Submit and Cancel buttons side by side
# cols = st.columns([4, 1, 1, 4])  # Adjust widths for spacing and button alignment
# with cols[1]:
#     submit_clicked = st.button("Submit")
# with cols[2]:
#     cancel_clicked = st.button("Cancel")

# # Handle Submit button click
# if submit_clicked:
#     db_status = insert_data_to_db(data)
#     st.success("Submitted successfully!")
#     st.info(db_status)
# elif cancel_clicked:
#     st.warning("Action canceled!")





















# import streamlit as st
# import mysql.connector
# from mysql.connector import Error

# # Set page configuration
# st.set_page_config(page_title="Dynamic Fabric Capacity Management", layout="wide")

# # Function to insert data into MySQL
# def insert_data_to_db(data):
#     try:
#         # Establish MySQL connection
#         connection = mysql.connector.connect(
#             host="demodb.cvio4iq4uq97.ap-southeast-2.rds.amazonaws.com",        
#             user="admin",   
#             password="Admin123",
#             database="demo"   
#         )

#         if connection.is_connected():
#             cursor = connection.cursor()
#             # SQL query to insert data
#             for entry in data:
#                 query = """
#                 INSERT INTO fabric_capacity (start_time, end_time, capacity)
#                 VALUES (%s, %s, %s)
#                 """
#                 cursor.execute(query, (entry["Start Time"], entry["End Time"], entry["Capacity"]))
#             connection.commit()
#             return " "
#     except Error as e:
#         return f"Error connecting to MySQL: {str(e)}"
#     finally:
#         if connection.is_connected():
#             cursor.close()
#             connection.close()

# # Custom CSS for button and title styling
# st.markdown(
#     """
#     <style>
#     .button-style {
#         background-color: #55b6f9;
#         color: white;
#         font-size: 16px;
#         border: none;
#         border-radius: 5px;
#         padding: 10px 2px;
#         cursor: pointer;
#     }
#     .button-style:hover {
#         background-color: darkorange;
#     }
#     .title-style {
#         background-color: #ff7628;
#         color: white;
#         font-size: 28px;
#         font-weight: bold;
#         text-align: center;
#         padding: 10px 0;
#         border-radius: 8px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Display logo and title
# # Display logo and title
# cols = st.columns([1, 8, 1])  # Adjust widths for equal spacing
# # Display logo and title
# st.markdown(
#     """
#     <style>
#     .header-container {
#         display: flex;
#         justify-content: space-between;
#         align-items: center;
#         width: 100%;
#     }
#     .header-left img {
#         width: 120px;
#         margin-right: auto;
#     }
#     .header-center {
#         flex-grow: 1;
#         text-align: center;
#         font-size: 28px;
#         font-weight: bold;
#         color: white;
#         background-color: #ff7628;
#         padding: 10px 0;
#         border-radius: 8px;
#     }
#     .header-right img {
#         width: 80px;
#         margin-left: auto;
#     }
#     </style>
#     <div class="header-container">
#         <div class="header-left">
#             <img src="https://bgimg6384.s3.us-east-2.amazonaws.com/enoahlogo.png" alt="Left Logo">
#         </div>
#         <div class="header-center">
#             Dynamic Fabric Capacity Management
#         </div>
#         <div class="header-right">
#             <img src="https://bgimg6384.s3.us-east-2.amazonaws.com/fabriclogo.png" alt="Right Logo">
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )



# st.write("")  # Add spacing

# # Create three rows for Start Time, End Time, and Capacity
# data = []
# for i in range(3):
#     cols = st.columns([2, 2, 2])  # Define column widths
#     with cols[0]:
#         start_time = st.time_input(f"Start Time {i+1}", key=f"start_time_{i+1}")
#     with cols[1]:
#         end_time = st.time_input(f"End Time {i+1}", key=f"end_time_{i+1}")
#     with cols[2]:
#         capacity = st.selectbox(f"Fabric Capacity {i+1}", options=["F2", "F4", "F6"], key=f"capacity_{i+1}")
#     data.append({"Start Time": str(start_time), "End Time": str(end_time), "Capacity": capacity})

# st.write("")  # Add spacing

# # Create Submit and Cancel buttons side by side
# cols = st.columns([4, 1, 1, 4])  # Adjust widths for spacing and button alignment
# with cols[1]:
#     submit_clicked = st.button("Submit")
# with cols[2]:
#     cancel_clicked = st.button("Cancel")

# # Handle Submit button click
# if submit_clicked:
#     db_status = insert_data_to_db(data)
#     st.success("Submitted successfully!")
#     st.info(db_status)
# elif cancel_clicked:
#     st.warning("Action canceled!")



# updated




import streamlit as st
import mysql.connector
from mysql.connector import Error
from datetime import datetime, time

# Set page configuration
st.set_page_config(page_title="Dynamic Fabric Capacity Management", layout="wide")

# Function to insert data into MySQL
def insert_data_to_db(data):
    try:
        # Establish MySQL connection
        connection = mysql.connector.connect(
            host="demodb.cvio4iq4uq97.ap-southeast-2.rds.amazonaws.com",
            user="admin",
            password="Admin123",
            database="demo"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # SQL query to insert data
            for entry in data:
                query = """
                INSERT INTO fabric_capacity (start_time, end_time, capacity)
                VALUES (%s, %s, %s)
                """
                cursor.execute(query, (entry["Start Time"], entry["End Time"], entry["Capacity"]))
            connection.commit()
            return " "
    except Error as e:
        return f"Error connecting to MySQL: {str(e)}"
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Custom CSS for header styling
st.markdown(
    """
    <style>
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
        background-color: #ff7628; /* Background color */
        border-radius: 5px;
        padding: 0px;
    }
    .header-left img, .header-right img {
        height: 80px; /* Uniform height for logos */
    }
    .header-center {
        flex-grow: 1;
        text-align: center;
        font-size: 28px;
        font-weight: bold;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display the header with logos and title
st.markdown(
    """
    <div class="header-container">
        <div class="header-left">
            <img src="https://bgimg6384.s3.us-east-2.amazonaws.com/enoahlogo.png" alt="Left Logo">
        </div>
        <div class="header-center">
            Dynamic Fabric Capacity Management
        </div>
        <div class="header-right">
            <img src="https://bgimg6384.s3.us-east-2.amazonaws.com/fabriclogo.png" alt="Right Logo">
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")  # Add spacing

# Default data
default_data = [
    {"Start Time": "08:00", "End Time": "12:00", "Capacity": "F6"},
    {"Start Time": "12:00", "End Time": "18:00", "Capacity": "F4"},
    {"Start Time": "18:00", "End Time": "23:00", "Capacity": "F2"},
]

# Convert string time to datetime.time
for default in default_data:
    default["Start Time"] = datetime.strptime(default["Start Time"], "%H:%M").time()
    default["End Time"] = datetime.strptime(default["End Time"], "%H:%M").time()

# Input fields
st.markdown("**Note:** End time should be greater than Start time and times must not overlap with existing time ranges.", unsafe_allow_html=True)

data = []
invalid_entries = False
time_ranges = []

for i, default in enumerate(default_data):
    cols = st.columns([2, 2, 2])  # Define column widths
    with cols[0]:
        start_time = st.time_input(f"Start Time {i+1}", value=default["Start Time"], key=f"start_time_{i+1}")
    with cols[1]:
        end_time = st.time_input(f"End Time {i+1}", value=default["End Time"], key=f"end_time_{i+1}")
    with cols[2]:
        capacity = st.selectbox(
            f"Fabric Capacity {i+1}",
            options=["F2", "F4", "F6"],
            index=["F2", "F4", "F6"].index(default["Capacity"]),
            key=f"capacity_{i+1}",
        )

    # Validation logic
    if end_time <= start_time:
        st.error(f"End Time {i+1} must be greater than Start Time {i+1}.")
        invalid_entries = True

    # Check for overlapping time ranges
    overlap = False
    for existing_start, existing_end in time_ranges:
        if (start_time >= existing_start and start_time < existing_end) or \
           (end_time > existing_start and end_time <= existing_end) or \
           (start_time <= existing_start and end_time >= existing_end):
            overlap = True
            break

    if overlap:
        st.error(f"Time range for {i+1} overlaps with an existing range. Please adjust the times.")
        invalid_entries = True
    else:
        time_ranges.append((start_time, end_time))

    data.append({"Start Time": str(start_time), "End Time": str(end_time), "Capacity": capacity})

st.write("")  # Add spacing

# Create Submit and Cancel buttons side by side
cols = st.columns([4, 1, 1, 4])  # Adjust widths for spacing and button alignment
with cols[1]:
    submit_clicked = st.button("Submit")
with cols[2]:
    cancel_clicked = st.button("Cancel")

# Handle Submit button click
if submit_clicked:
    if invalid_entries:
        st.error("Please adjust the times correctly before submitting.")
    else:
        db_status = insert_data_to_db(data)
        st.success("Submitted successfully!")
        st.info(db_status)
elif cancel_clicked:
    st.warning("Action canceled!")

 
