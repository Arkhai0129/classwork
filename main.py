import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from supabase import create_client, Client

url: str = "https://xiachjnxrcqqvlkquazq.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhpYWNoam54cmNxcXZsa3F1YXpxIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDE4Mzk3OTgsImV4cCI6MjA1NzQxNTc5OH0.2e8TrRYic61lJh3hs1oPqQegQSmzjC_NBySAQzKSq6E"

supabase: Client = create_client(url, key)

app = FastAPI()

class Item(BaseModel):
    company: str
    specific_bean_origin_or_bar_name: str = None
    ref: int
    review_date: int
    cocoa_percent: str
    company_location: str
    rating: int
    bean_type: str
    broad_bean_origin: str

@app.get("/items/")
def read_items():
    data = supabase.table("chocolate_bar_rows").select("*").execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Items not found")


@app.post("/items/")
def create_item(item: Item):
    data = supabase.table("chocolate_bar_rows").insert(item.dict()).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=400, detail="Item could not be created")


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    data = supabase.table("chocolate_bar_rows").update(item.dict()).eq("id", item_id).execute()
    if data.data:
        return data.data
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    data = supabase.table("chocolate_bar_rows").delete().eq("id", item_id).execute()
    if data.data:
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")




