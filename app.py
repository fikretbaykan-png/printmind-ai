from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PrintMind AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "PrintMind AI çalışıyor"}

@app.post("/api/quote")
def quote(
    customer_name: str = Form(""),
    customer_phone: str = Form(""),
    customer_email: str = Form(""),
    message: str = Form("")
):
    return {
        "status": "success",
        "customer_name": customer_name,
        "customer_phone": customer_phone,
        "customer_email": customer_email,
        "message": message,
        "price": 915,
        "note": "Test backend çalışıyor. Sonraki adımda gerçek fiyat motoru bağlanacak."
    }
