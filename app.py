import pandas as pd
import numpy as np
import streamlit as st
import streamlit as st

st.title("Hello")


class Preditors:
    def __init__(self,name, shape, size, colour, aggressive):
        self.name = name
        self.shape = shape
        self.size = size
        self.colour = colour
        self.aggressive = aggressive

def predict():
    pass

def get_monty_attributes():
    name = "Monty"
    size = "big"
    shape = "elongated"
    aggressive = True
    colour = "brown"
    return {"name": name, "size": size, "colour": colour, "shape": shape, "aggressive": aggressive}

def get_calif_attributes():
    name = "Calif"
    size = "small"
    shape = "rounded"
    aggressive = False
    colour = "grey"
    return {"name": name, "size": size, "colour": colour, "shape": shape, "aggressive": aggressive}

calif_attributes = get_calif_attributes()
monty_attributes = get_monty_attributes()

calif = Preditors(**calif_attributes)
monty = Preditors(**monty_attributes)

predators = [calif, monty]
predator_by_name = {"calif": calif, "monty": monty}

search_size = input("Enter predator size (e.g., big, small): ").lower()
search_shape = input("Enter the shape of the predator (e.g., elongated, rounded): ").lower()
search_colour = input("Enter the colour of the predator (e.g., brown, grey): ").lower()
search_aggressive = input("Is the predator aggressive? (yes/no): ").lower()

search_aggressive_str = search_aggressive
search_aggressive = False
if search_aggressive_str == "yes":
    search_aggressive = True

user_search_criteria = {
    "size": search_size,
    "shape": search_shape,
    "colour": search_colour,
    "aggressive": search_aggressive,
}
print(f"User search criteria: {user_search_criteria}")

found_predator = None
for predator in predators:
    if (
        predator.size == search_size
        and predator.shape == search_shape
        and predator.colour == search_colour
        and predator.aggressive == search_aggressive
    ):
        found_predator = predator
        break


if found_predator:
    print(f"\nIdentified Predator: {found_predator.name}")
else:
    print("\nNo predator found matching the provided criteria.")