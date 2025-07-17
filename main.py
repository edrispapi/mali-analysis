from fastapi import FastAPI
from routers import router as api_router

app = FastAPI(
    title="Advanced Core Financial Platform",
    version="1.0.0",
    description="Enterprise-grade Forex market analytics API"
)

# ثبت تمام مسیریاب‌ها و کنترل کننده‌ها
app.include_router(api_router, prefix="/api")

@app.get("/")
def health_check():
    """نمایش سلامت سامانه"""
    return {"status": "ok", "message": "Forex Analytics Platform is Running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
