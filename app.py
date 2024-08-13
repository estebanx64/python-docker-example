from fastapi import FastAPI
from payslip_creator import pdf_payslip_creator

app = FastAPI()

@app.get("/")

async def root(jsonData: dict):

    result = pdf_payslip_creator(jsonData)

    return result
