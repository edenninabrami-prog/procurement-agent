from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional

app = FastAPI(title="Supplier External Agent", description="Stateless external-info agent")

NO_DATA_MSG = "אין כרגע מידע זמין במקורות החיצוניים שלי לגבי השאלה הזו."
PRIVACY_NOTE = "Stateless: לא שומר שיחות. קבצים מצורפים—שימוש חד-פעמי ומחיקה."

@app.get("/health")
def health():
    return {"status": "ok", "note": PRIVACY_NOTE}

@app.post("/ask")
async def ask(
    query: str = Form(...),
    category: Optional[str] = Form(None),
    region: Optional[str] = Form(None),
    year: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    # בשלב זה עוד אין מקורות – נחזיר תשובת ברירת מחדל שקופה
    return {
        "query": query,
        "filters": {"category": category, "region": region, "year": year},
        "results": [],
        "message": NO_DATA_MSG,
        "privacy": PRIVACY_NOTE
    }