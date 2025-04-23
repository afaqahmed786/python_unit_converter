import streamlit as st

# Page config
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Title and description
st.title("🔄 Universal Unit Converter")
st.markdown("Convert **Length**, **Weight**, and **Temperature** easily and interactively.")

# Unit conversion data
unit_categories = {
    "Length": {
        "units": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
        "factors": {
            "Meter": 1,
            "Kilometer": 1000,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254,
        }
    },
    "Weight": {
        "units": ["Kilogram", "Gram", "Pound", "Ounce"],
        "factors": {
            "Kilogram": 1,
            "Gram": 0.001,
            "Pound": 0.453592,
            "Ounce": 0.0283495,
        }
    },
    "Temperature": {
        "units": ["Celsius", "Fahrenheit", "Kelvin"]
    }
}

# Dropdown for category
category = st.selectbox("Select Category", list(unit_categories.keys()))

col1, col2 = st.columns(2)

with col1:
    from_unit = st.selectbox("From", unit_categories[category]["units"])
with col2:
    to_unit = st.selectbox("To", unit_categories[category]["units"])

value = st.number_input("Enter value", min_value=0.0, format="%.4f")

def convert_units(category, from_u, to_u, val):
    if category in ["Length", "Weight"]:
        base = val * unit_categories[category]["factors"][from_u]
        result = base / unit_categories[category]["factors"][to_u]
        return result
    elif category == "Temperature":
        if from_u == to_u:
            return val
        # Celsius to others
        if from_u == "Celsius":
            if to_u == "Fahrenheit":
                return (val * 9/5) + 32
            elif to_u == "Kelvin":
                return val + 273.15
        # Fahrenheit to others
        elif from_u == "Fahrenheit":
            if to_u == "Celsius":
                return (val - 32) * 5/9
            elif to_u == "Kelvin":
                return (val - 32) * 5/9 + 273.15
        # Kelvin to others
        elif from_u == "Kelvin":
            if to_u == "Celsius":
                return val - 273.15
            elif to_u == "Fahrenheit":
                return (val - 273.15) * 9/5 + 32

result = convert_units(category, from_unit, to_unit, value)

st.markdown(f"### ✅ Result: `{value} {from_unit}` = **{round(result, 4)} {to_unit}**")

st.markdown("---")
st.caption("Made with ❤️ using Python & Streamlit")
