import streamlit as st
from llm import get_llm
from prompts import get_resume_prompt
from util import clean_json_response, parse_json_safe

# Init
llm = get_llm()

st.set_page_config(page_title="AI Resume Bot", page_icon="🧠")
st.title("AI Resume Generator")

# -------------------------
# Step-by-step form
# -------------------------

if "name" not in st.session_state:
    name = st.text_input("What is your name?")
    if name.strip():
        st.session_state.name = name.strip()
        st.rerun()
    else:
        st.warning("Name is required")

elif "age" not in st.session_state:
    age = st.text_input("What is your age?")
    if age.strip():
        if age.isdigit():
            st.session_state.age = int(age)
            st.rerun()
        else:
            st.error("Enter valid age")

elif "email" not in st.session_state:
    email = st.text_input("What is your email?")
    if email.strip():
        if "@" in email:
            st.session_state.email = email.strip()
            st.rerun()
        else:
            st.error("Invalid email")

elif "role" not in st.session_state:
    role = st.text_input("Enter your role")
    if role.strip():
        st.session_state.role = role.strip()
        st.rerun()
    else:
        st.warning("Role required")

# -------------------------
# Generate Resume
# -------------------------

else:
    st.success("All data collected ✅")

    if st.button("Generate Resume"):

        prompt = get_resume_prompt()
        chain = prompt | llm

        response = chain.invoke({
            "name": st.session_state.name,
            "age": st.session_state.age,
            "email": st.session_state.email,
            "role": st.session_state.role
        })

        raw = response.content

        cleaned = clean_json_response(raw)
        data, error = parse_json_safe(cleaned)

        if error:
            st.error("JSON parsing failed")
            st.code(cleaned)
        else:
            st.subheader("Your Resume")

            st.write("Name:", data.get("name"))
            st.write("Email:", data.get("email"))
            st.write("Summary:", data.get("summary"))
            st.write("Skills:", ", ".join(data.get("skills", [])))
            st.write("Experience:", data.get("experience"))

            st.download_button(
                label="Download JSON",
                data=cleaned,
                file_name="resume.json",
                mime="application/json"
            )

    if st.button("Start Over"):
        st.session_state.clear()
        st.rerun()