from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

app = FastAPI()

# Allow React frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UrlRequest(BaseModel):
    url: str

@app.post("/api/scrap")
async def scrape_website(data: UrlRequest):
    url = data.url

    # Install the correct ChromeDriver automatically
    chromedriver_autoinstaller.install()

    # --- Setup Selenium ---
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        driver.quit()

        # ✅ Return only the success message
        return {"message": "Website scraped successfully!"}

    except Exception as e:
        return {"error": str(e)}
