import pandas as pd
import numpy as np
import streamlit as st
import streamlit as st

st.title("Hello")


import streamlit as st

# ---------------- UI HEADER ----------------
st.title("🐛 Predator Finder & Analysis App")
st.write("Find and analyze predator types based on attributes.")

# ---------------- CLASS ----------------
class Preditors:
    def __init__(self, name, shape, size, colour, aggressive):
        self.name = name
        self.shape = shape
        self.size = size
        self.colour = colour
        self.aggressive = aggressive


# ---------------- DATA ----------------
def get_monty_attributes():
    return {
        "name": "Monty",
        "size": "big",
        "shape": "elongated",
        "aggressive": True,
        "colour": "brown"
    }


def get_calif_attributes():
    return {
        "name": "Calif",
        "size": "small",
        "shape": "rounded",
        "aggressive": False,
        "colour": "grey"
    }


calif = Preditors(**get_calif_attributes())
monty = Preditors(**get_monty_attributes())

predators = [calif, monty]

# ---------------- INPUT SECTION ----------------
st.subheader("🔎 Search Predator")

search_size = st.selectbox("Size", ["small", "big"])
search_shape = st.selectbox("Shape", ["rounded", "elongated"])
search_colour = st.selectbox("Colour", ["grey", "brown"])
search_aggressive = st.selectbox("Aggressive?", ["yes", "no"])

search_aggressive_bool = search_aggressive == "yes"

# ---------------- SEARCH BUTTON ----------------
if st.button("Find Predator"):

    found_predator = None

    for predator in predators:
        if (
            predator.size == search_size
            and predator.shape == search_shape
            and predator.colour == search_colour
            and predator.aggressive == search_aggressive_bool
        ):
            found_predator = predator
            break

    # ---------------- RESULT ----------------
    st.subheader("📊 Result")

    if found_predator:
        st.success(f"Identified Predator: {found_predator.name}")

        st.write("### Details")
        st.write(f"🟢 Size: {found_predator.size}")
        st.write(f"🟢 Shape: {found_predator.shape}")
        st.write(f"🟢 Colour: {found_predator.colour}")
        st.write(f"🟢 Aggressive: {found_predator.aggressive}")

    else:
        st.error("No predator found matching your criteria.")