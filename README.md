# 🏋️ FitGenie AI – Personalized Fitness Buddy

An AI-powered Fitness & Wellness Assistant developed using **IBM watsonx.ai**, **IBM watsonx Orchestrate**, **IBM Granite Foundation Models**, and **Streamlit**. The application provides personalized workout plans, healthy meal recommendations, hydration guidance, motivational coaching, and healthy lifestyle suggestions based on user inputs.

---

## 📌 Project Overview

Maintaining a healthy lifestyle can be difficult due to busy schedules, lack of personalized guidance, and inconsistent motivation. FitGenie AI addresses these challenges by acting as an intelligent virtual fitness coach that provides customized recommendations tailored to each user's fitness goals and personal profile.

The project was developed as part of the **IBM University Engagement Internship** using IBM Cloud technologies.

---

## 🎯 Problem Statement

Many individuals struggle to:

- Build effective workout routines
- Maintain healthy eating habits
- Stay motivated consistently
- Receive personalized fitness guidance
- Access affordable fitness coaching

FitGenie AI provides an intelligent and accessible solution using IBM's AI technologies.

---

## 💡 Proposed Solution

FitGenie AI collects user information such as:

- Age
- Gender
- Height
- Weight
- Fitness Goal
- Activity Level
- Workout Preference
- Diet Preference

Using IBM Foundation Models, the application generates:

- 🏋️ Personalized Workout Plans
- 🥗 Healthy Meal Recommendations
- 💧 Daily Water Intake Suggestions
- 🔥 Calorie Guidance
- 😊 Daily Motivation
- 💤 Recovery Tips
- ❤️ Healthy Lifestyle Recommendations

---

# 🚀 Features

- AI-powered personalized fitness assistant
- Intelligent workout recommendations
- Healthy meal planning
- Hydration guidance
- Motivation and habit building
- Simple and user-friendly Streamlit interface
- IBM watsonx Orchestrate Agent integration
- IBM Granite Foundation Model support
- Knowledge base integration using IBM Orchestrate

---

# 🛠 Technologies Used

- IBM Cloud
- IBM watsonx.ai
- IBM watsonx Orchestrate
- IBM Granite Foundation Models
- IBM Prompt Lab
- Python
- Streamlit
- GitHub
- python-dotenv
- requests
- ibm-watsonx-ai SDK

---

# 🏗 System Architecture

```
                User
                  │
                  ▼
        Streamlit Web Application
                  │
                  ▼
      IBM watsonx Orchestrate Agent
                  │
                  ▼
      IBM Granite Foundation Model
                  │
                  ▼
       Fitness Knowledge Base
                  │
                  ▼
 Personalized Fitness Recommendation
```

---

# 📂 Project Structure

```
FitGenie-AI/

│── app.py
│── ibm_ai.py
│── config.py
│── requirements.txt
│── README.md
│── .env
│── .gitignore

├── assets/
├── screenshots/
├── knowledge/
│     └── FitGenie_AI_Fitness_Guide.pdf
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/FitGenie-AI.git

cd FitGenie-AI
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```env
IBM_API_KEY=YOUR_API_KEY

IBM_PROJECT_ID=YOUR_PROJECT_ID

IBM_URL=YOUR_WATSONX_URL

MODEL_ID=ibm/granite-4-h-small
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 🌟 Advantages

- Personalized fitness guidance
- Affordable AI fitness coach
- 24×7 availability
- Easy to use
- Scalable cloud architecture
- Supports healthy lifestyle habits
- Can be extended with wearable devices

---

# 🔮 Future Scope

- Mobile application
- Voice assistant integration
- Smartwatch connectivity
- Real-time health monitoring
- AI progress tracking
- Multilingual support
- Integration with healthcare professionals
- Exercise video recommendations
- Cloud deployment
- Personalized health analytics

---

# 👨‍💻 Developer

**Abhilash Gandesri**

B.Tech – Computer Science & Engineering (AI & ML)

IBM University Engagement Internship

---

# 📜 License

This project was developed for educational and internship purposes under the IBM University Engagement Program.

---

# 🙏 Acknowledgements

- IBM Cloud
- IBM watsonx.ai
- IBM watsonx Orchestrate
- IBM Granite Foundation Models
- IBM SkillsBuild
- Streamlit Community
