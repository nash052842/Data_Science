from turtle import speed

from numpy import tan
import streamlit as st

st.title("🕷️ Predator Finder & Analysis App")

# ---------------- STATE ----------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ---------------- INPUT FORM ----------------
if not st.session_state.submitted:

    st.subheader("🔎 Enter Search Criteria")

    search_size = st.selectbox("Size", ["small", "big"])
    search_shape = st.selectbox("Shape", ["rounded", "elongated"])
    search_colour = st.selectbox("Colour", ["grey", "brown"])
    search_aggressive = st.selectbox("Aggressive?", ["yes", "no"])

    if st.button("Find Predator"):
        st.session_state.search_size = search_size
        st.session_state.search_shape = search_shape
        st.session_state.search_colour = search_colour
        st.session_state.search_aggressive = (search_aggressive == "yes")
        st.session_state.submitted = True
        st.rerun()

# ---------------- RESULT SECTION ----------------
else:
    st.subheader("📊 Result")

    class Preditors:
        def __init__(self, name, shape, size, colour, aggressive,development_speed,Moderate,High,BeigeTan,Reproduction_rate,Pale_transparent,Light_tan,Pear_shaped,Oval_to_teardrop,Broad_oval,Oval_slender):
            self.name = name
            self.shape = shape
            self.size = size
            self.colour = colour
            self.aggressive = aggressive
            self.speed = development_speed
            self.Moderate = Moderate
            self.High = High    
            self.Beige_Tan = BeigeTan
            self.Reproduction_rate = Reproduction_rate
            self.Pale_transparent = Pale_transparent
            self.Light_tan = Light_tan  
            self.Pear_shaped = Pear_shaped
            self.Oval_to_teardrop = Oval_to_teardrop    
            self.Broad_oval = Broad_oval
            self.Oval_slender = Oval_slender

    def get_monty_attributes():
        return {
            "name": "Monty",
            "size": "medium",
            "shape": "oval_slender",
            "colour": "creamy_tan",
            "aggressive": True,
            "development_speed": "Fast"
        }

    def get_calif_attributes():
        return {
            "name": "Calif",
            "size": "medium",
            "shape": "oval_to_teardrop",
            "colour": "grey",
            "aggressive": False,
            "development_speed": "moderate"
        }

    def get_cucumeris_attributes():
        return {
            "name": "Cucumeris",
            "size": "medium",
            "shape": "pear_shaped",
            "colour": "light_tan",
            "aggressive": False,
            "development_speed": "Moderate",
            "colour": "beige_tan",
        }

    def get_swirskii_attributes():
        return {
            "name": "Swirskii",
            "size": "medium",
            "shape": "broad_oval",
            "colour": "light_tan",
            "aggressive": True,
            "development_speed": "Fast"
        }
    calif = Preditors(**get_calif_attributes())
    monty = Preditors(**get_monty_attributes())
    cucumeris = Preditors(**get_cucumeris_attributes())
    swirskii = Preditors(**get_swirskii_attributes())

    predators = [calif, monty, cucumeris, swirskii]

    found_predator = None

    for predator in predators:
        if (
            predator.size == st.session_state.search_size
            and predator.shape == st.session_state.search_shape
            and predator.colour == st.session_state.search_colour
            and predator.aggressive == st.session_state.search_aggressive
        ):
            found_predator = predator
            break

    if found_predator:
        st.success(f"Identified Predator: {found_predator.name}")

        st.write("### Details")
        st.write(f"Size: {found_predator.size}")
        st.write(f"Shape: {found_predator.shape}")
        st.write(f"Colour: {found_predator.colour}")
        st.write(f"Aggressive: {found_predator.aggressive}")
        st.write(f"Development Speed: {found_predator.speed}")
        

    else:
        st.error("No predator found")

    if st.button("🔄 New Search"):
        st.session_state.submitted = False
        st.rerun()