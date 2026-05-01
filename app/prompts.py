from langchain_core.prompts import ChatPromptTemplate

def get_resume_prompt():
    return ChatPromptTemplate.from_template("""
You are a professional resume writer.

Generate a DETAILED and PROFESSIONAL resume in JSON format.

Make sure:
- Summary is 4-5 lines
- Skills are detailed (not just 1 word)
- Experience is well explained (at least 4-5 lines)

User:
Name: {name}
Age: {age}
Email: {email}
Role: {role}

Return ONLY valid JSON.

Format:
{{
  "name": "",
  "summary": "",
  "skills": [],
  "experience": "",
  "email": ""  
}}
""")