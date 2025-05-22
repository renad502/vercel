from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def health_check():
    return "The health check is successful"

@app.get("/status", response_class=HTMLResponse)
async def status_check():
    html_content = """
    <html>
        <head>
            <title>Health Status</title>
            <style>
                body {
                    background-color: #f0f8ff;
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                }
                .status {
                    font-size: 24px;
                    color: green;
                    border: 2px solid #4CAF50;
                    padding: 20px;
                    border-radius: 10px;
                    display: inline-block;
                    background-color: #e6ffe6;
                }
            </style>
        </head>
        <body>
            <div class="status">
                The service is up and running smoothly!
            </div>
        </body>
    </html>
    """
    return html_content
