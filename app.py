import streamlit as st

st.title("🧪 LDL Cholesterol Calculator")

st.write("Calculate LDL cholesterol using the Friedewald equation.")

st.divider()

total_cholesterol = st.number_input(
    "Total Cholesterol (mmol/L)",
    min_value=0.0,
    value=5.2,
    step=0.1
)

triglycerides = st.number_input(
    "Triglycerides (mmol/L)",
    min_value=0.0,
    value=1.7,
    step=0.1
)

hdl = st.number_input(
    "HDL Cholesterol (mmol/L)",
    min_value=0.0,
    value=1.3,
    step=0.1
)

if st.button("Calculate LDL"):

    ldl = total_cholesterol - hdl - (triglycerides / 2.2)

    st.success(f"Estimated LDL: {ldl:.2f} mmol/L")