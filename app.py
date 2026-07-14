import streamlit as st

st.set_page_config(
    page_title="FitGenie AI",
    page_icon="🏋️",
    layout="wide"
)

st.title("🏋️ FitGenie AI")
st.subheader("AI-Powered Fitness & Wellness Coach")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("👤 Personal Information")

    age = st.number_input("Age", 10, 80, 21)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    height = st.number_input(
        "Height (cm)",
        100,
        250,
        170
    )

    weight = st.number_input(
        "Weight (kg)",
        30,
        200,
        65
    )

with col2:

    st.header("🎯 Fitness Goals")

    goal = st.selectbox(
        "Fitness Goal",
        [
            "Weight Loss",
            "Muscle Gain",
            "Maintain Fitness"
        ]
    )

    activity = st.selectbox(
        "Activity Level",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    workout = st.selectbox(
        "Workout Preference",
        [
            "Home Workout",
            "Gym Workout"
        ]
    )

    diet = st.selectbox(
        "Diet Preference",
        [
            "Vegetarian",
            "Non-Vegetarian"
        ]
    )

generate = st.button("🚀 Generate Fitness Plan")

st.markdown("---")

st.header("🤖 AI Recommendation")
from ibm_ai import generate_plan
if generate:

    prompt = f"""
    Age: {age}

    Gender: {gender}

    Height: {height}

    Weight: {weight}

    Goal: {goal}

    Activity Level: {activity}

    Workout: {workout}

    Diet: {diet}

    Generate

    1 Workout Plan

    2 Diet Plan

    3 Water Intake

    4 Calories

    5 Motivation

    6 Recovery Tips
    """

    with st.spinner("Generating Fitness Plan..."):

        answer = generate_plan(prompt)

    st.success("Fitness Plan Generated Successfully!")
    st.write(answer)