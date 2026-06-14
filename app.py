from fastapi import FastAPI,UploadFile
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import os
app=FastAPI()
def extract_text(pdf_path):
    reader=PdfReader(pdf_path)
    text=""
    for page in reader.pages:
        page_text=page.extract_text()
        if page_text:
            text+=page_text
    return text
@app.get("/")
def home():
    return {
        "message":"Resume Analyzer Running"
    
    }

#upload resume api
@app.post("/upload")
async def upload_resume(file:UploadFile):
    global resume_text_store
    os.makedirs("resumes",exist_ok=True)
    path=f"resumes/{file.filename}"
    contents=await file.read()
    with open(path,"wb")as f:
        f.write(contents)
    resume_text_store=extract_text(path)
    return {
        "filename":"Resume Uploaded"
    }
#loaded model
model=SentenceTransformer("all-MiniLM-L6-v2")
def get_similarity(resume_text,job_text):
    resume_embedding=model.encode(resume_text).reshape(1,-1)
    job_embedding=model.encode([job_text]).reshape(1,-1)
    score=cosine_similarity(resume_embedding,job_embedding)[0][0]
    return round(score*100,2)


skills=["python","java","c++","fastapi","django","flask","docker","kubernetes","aws","git","github","sql","mysql","mangodb","machine learning","deep learning","nlp","rag","langchain","langgraph"]
#skill extractor
def extract_skills(text):
    text=text.lower()
    found=[]
    for skill in skills:
        if skill in text:
            found.append(skill)
    return list(set(found))
@app.get("/analyze")
def analyze(job_description:str):
    print("JOB DESCRIPTION: ",job_description)
    if "resume_text_store" not in globals():
        return {"error":"Upload resume first"}
    
    score=get_similarity(resume_text_store,job_description)
    resume_skills=extract_skills(resume_text_store)
    job_skills=extract_skills(job_description)
    print("RESUME SKILLS=",resume_skills)
    print("JOB Skills",job_skills)
    missing_skills=list(set(job_skills)-set(resume_skills))
    suggestions=[f"Learn {skill}"
                 for skill in missing_skills]
    
    return {"match_score":f"{score}%",
            "resume_skills":resume_skills,
            "job_skills":job_skills,
            "missing_skills":missing_skills,
            "suggestions":suggestions}
