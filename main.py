from fastapi import FastAPI, UploadFile, Form, HTTPException
import requests

app = FastAPI()

# Configuration
PRODUCT_ID = "YOUR_PRODUCT_ID_HERE" 

def verify_license(key: str) -> bool:
    url = f"https://payhip.com/api/v1/license/verify?product_id={PRODUCT_ID}&license_key={key}"
    try:
        response = requests.get(url, timeout=5)
        return response.status_code == 200 and response.json().get('status') == 'success'
    except:
        return False

@app.post("/verify")
async def verify(file: UploadFile, key: str = Form(...)):
    # 1. License Check
    if not verify_license(key):
        raise HTTPException(status_code=403, detail={"code": "BPS_403", "msg": "License denied"})
    
    # 2. File Check
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=422, detail={"code": "BPS_422", "msg": "Invalid file format"})
    
    # 3. Model Processing
    try:
        # INSERT MODEL LOGIC HERE
        return {"code": "BPS_200", "status": "Success", "file": file.filename}
    except:
        raise HTTPException(status_code=500, detail={"code": "BPS_500", "msg": "Engine Fault"})
