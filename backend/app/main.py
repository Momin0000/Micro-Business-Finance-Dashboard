from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

# Initialize FastAPI app
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]  # Replace with your database name

# Include your routes here

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}
