import pandas as pd
import numpy as np
import streamlit as st
import streamlit as st

st.title("Hello")


import streamlit as st

class Preditors:
    def __init__(self, name, shape, size, colour, aggressive):
        self.name = name
        self.shape = shape
        self.size = size
        self.colour = colour
        self.aggressive = aggressive


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


# Create objects
calif = Preditors(**get_calif_attributes())
monty = Preditors(**get_monty_attributes())

predators = [calif, monty]

# UI
st.title("🕷️ Predator Finder & Analysis App")

search_size = st.text_input("Enter predator size (big/small)").lower()
search_shape = st.text_input("Enter shape (elongated/rounded)").lower()
search_colour = st.text_input("Enter colour (brown/grey)").lower()
search_aggressive = st.selectbox("Aggressive?", ["yes", "no"])

search_aggressive_bool = search_aggressive == "yes"

if st.button("Search"):
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

    if found_predator:
        st.success(f"Identified Predator: {found_predator.name}")
    else:
        st.error("No predator found matching the provided criteria.")