import pandas as pd
import numpy as np
import streamlit as st
import streamlit as st

st.title("Hello")


import streamlit as st

# initialize state
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.title("🕷️ Predator Finder & Analysis App")


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

    # recreate your objects here (important)
    class Preditors:
        def __init__(self, name, shape, size, colour, aggressive):
            self.name = name
            self.shape = shape
            self.size = size
            self.colour = colour
            self.aggressive = aggressive

    def get_monty_attributes():
        return {"name": "Monty", "size": "big", "shape": "elongated", "aggressive": True, "colour": "brown"}

    def get_calif_attributes():
        return {"name": "Calif", "size": "small", "shape": "rounded", "aggressive": False, "colour": "grey"}

    calif = Preditors(**get_calif_attributes())
    monty = Preditors(**get_monty_attributes())

    predators = [calif, monty]

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

    else:
        st.error("No predator found")

    if st.button("🔄 New Search"):
        st.session_state.submitted = False
        st.rerun()