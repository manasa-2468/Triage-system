import streamlit as st

# Title
st.title("🏥 Smart Hospital Triage System")

# Input fields (same as your HTML form)
name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=0, step=1)
symptoms = st.number_input("Number of Symptoms", min_value=0, step=1)

# Button
if st.button("Check Patient Condition"):

    # Validation
    if name.strip() == "":
        st.error("Please enter patient name")
    elif age <= 0:
        st.error("Please enter valid age")
    else:
        # Your original logic
        if symptoms >= 8:
            result = "🚨 Critical Condition – Send patient to ICU immediately"
            st.error(result)

        elif 4 <= symptoms <= 7:
            result = "⚠️ Patient should stay in hospital for observation"
            st.warning(result)

        elif 2 <= symptoms <= 3:
            result = "💊 Doctor checkup required, patient can go home with medicine"
            st.info(result)

        else:
            result = "✅ No serious symptoms"
            st.success(result)

        # Optional: show summary
        st.write("### Patient Summary")
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Symptoms: {symptoms}")
