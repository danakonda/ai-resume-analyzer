# AI Resume Analyzer 

## Overview

AI Resume Analyzer V2 is a Generative AI project that analyzes a candidate's resume against a job description using semantic similarity and skill matching.

The application extracts text from PDF resumes, identifies technical skills, calculates an ATS-style match score, detects missing skills, and provides improvement suggestions.

---

## Features

- Upload Resume PDF
- Extract Resume Text
- Semantic Similarity Matching
- ATS-Style Match Score
- Skill Extraction
- Missing Skills Detection
- Resume Improvement Suggestions
- FastAPI Backend
- Streamlit Frontend
- Docker Ready

---

## Project Architecture

Resume PDF
↓
Text Extraction
↓
Skill Extraction
↓
Embedding Generation
↓
Job Description Embedding
↓
Cosine Similarity
↓
Match Score
↓
Skill Gap Analysis
↓
Suggestions

---

## Technologies Used

### Backend

- Python
- FastAPI

### Frontend

- Streamlit

### AI / NLP

- Sentence Transformers
- all-MiniLM-L6-v2
- Scikit-Learn

### PDF Processing

- PyPDF

### Deployment

- Docker
- Render

---

## Folder Structure

ai-resume-analyzer/

├── app.py

├── frontend.py

├── requirements.txt

├── Dockerfile

├── README.md

├── resumes/

└── screenshots/

---

## Installation

### Clone Repository

git clone https://github.com/danakonda/ai-resume-analyzer.git

cd ai-resume-analyzer

### Create Virtual Environment

python -m venv venv

### Activate Environment

Windows

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

---

## Run Backend

uvicorn app:app --reload

Backend URL:

http://localhost:8000

---

## Run Frontend

streamlit run frontend.py

Frontend URL:

http://localhost:8501

---

## API Endpoints

### Home

GET /

Returns application status.

### Upload Resume

POST /upload

Uploads a PDF resume and extracts text.

### Analyze Resume

GET /analyze

Parameters:

job_description

Returns:

- Match Score
- Resume Skills
- Job Skills
- Missing Skills
- Suggestions

---

## Example Output

Match Score: 82%

### Resume Skills

- Python
- FastAPI
- SQL
- Git

### Job Skills

- Python
- FastAPI
- Docker
- AWS

### Missing Skills

- Docker
- AWS

### Suggestions

- Learn Docker
- Learn AWS

---

## Future Improvements

- Gemini API Integration
- OpenAI API Integration
- Advanced ATS Scoring
- Resume Section Detection
- Skill Recommendation Engine
- Interactive Charts
- User Authentication
- Resume Ranking System

---

## Screenshots

Add screenshots inside:

screenshots/

Examples:

- Home Page
- Resume Upload
- Analysis Results
- Skill Gap Analysis

---

## Learning Outcomes

This project demonstrates:

- Natural Language Processing
- Embeddings
- Semantic Search
- Cosine Similarity
- FastAPI Development
- Streamlit Development
- Docker Deployment
- AI Application Development

---

## Author

Rajasekhar

B.Tech Computer Science Engineering

Generative AI | Python | FastAPI | RAG | AI Agents