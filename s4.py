# smart_grid_app.py
import streamlit as st
import pandas as pd
import numpy as np

# Simulated energy demand data (for demonstration purposes)
def generate_energy_demand():
    hours = np.arange(24)
    demand = np.random.randint(100, 500, size=24)  # Random demand values
    return pd.DataFrame({"Hour": hours, "Demand (MW)": demand})

def main():
    st.title("Smart Grid Management System")

    # Sidebar navigation
    menu = ["Home", "Sign Up", "Sign In", "Grid Management", "Log"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Home":
        st.header("Welcome to the Smart Grid Dashboard")
        st.markdown("Explore real-time energy data and analytics.")

    elif choice == "Sign Up":
        st.header("Sign Up")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if st.button("Create Account"):
            if password == confirm_password:
                # Save user data (e.g., to a database)
                st.success("Account created successfully!")
            else:
                st.error("Passwords do not match. Please try again.")

    elif choice == "Sign In":
        st.header("Sign In")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Log In"):
            # Authenticate user (e.g., check credentials in a database)
            # Redirect to dashboard if successful
            st.success("Logged in successfully!")
        else:
            st.warning("Invalid credentials. Please try again.")

    elif choice == "Grid Management":
        st.header("Grid Management")
        # Implement smart grid management features here

    elif choice == "Log":
        st.header("User Data and Demand Adjustment")
        # Display user data table
        # Allow users to adjust demand (MW)

        # Load energy demand data
        energy_demand_df = generate_energy_demand()
        user_input = st.slider("Adjust Demand (MW)", min_value=0, max_value=1000, value=500)
        predicted_demand = user_input * 0.9  # Placeholder prediction (adjust as needed)

        st.subheader("Real-Time Energy Distribution")
        st.markdown(f"Predicted Demand: {predicted_demand:.2f} MW")
        st.line_chart(energy_demand_df.set_index("Hour"))

        # Placeholder renewable energy integration
        st.subheader("Renewable Energy Sources")
        st.markdown("Integrating solar and wind power seamlessly...")

        # Display user data table (replace with actual user data)
        user_data = pd.DataFrame({"Username": ["jsmith", "rbriggs"],
                                  "Email": ["jsmith@gmail.com", "rbriggs@gmail.com"],
                                  "Name": ["John Smith", "Rebecca Briggs"]})
        st.subheader("User Data")
        st.dataframe(user_data)

if __name__ == "__main__":
    main()
