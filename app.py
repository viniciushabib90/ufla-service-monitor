from fastapi import FastAPI
import urllib.request
import urllib.error
import time

app = FastAPI(
    title="UFLA Service Monitor",
    description="Monitoramento de disponibilidade dos sistemas institucionais da UFLA",
    version="1.0.0"
)

SERVICES = {
    "SEI": "https://sei.ufla.br",
    "SIG": "https://sig.ufla.br",
    "Campus Virtual": "https://campusvirtual.ufla.br"
}


@app.get("/")
def home():
    return {
        "application": "UFLA Service Monitor",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/services")
def check_services():
    results = []

    for name, url in SERVICES.items():
        start = time.time()

        try:
            request = urllib.request.Request(
                url,
                headers={"User-Agent": "UFLA-Service-Monitor/1.0"},
                method="GET"
            )

            with urllib.request.urlopen(request, timeout=5) as response:
                status_code = response.status

            status = "UP" if status_code < 500 else "DOWN"

        except Exception:
            status_code = None
            status = "DOWN"

        response_time = round((time.time() - start) * 1000, 2)

        results.append({
            "name": name,
            "url": url,
            "status": status,
            "http_status": status_code,
            "response_time_ms": response_time
        })

    return {
        "total": len(results),
        "services": results
    }
