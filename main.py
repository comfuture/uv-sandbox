from uv_sandbox import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
