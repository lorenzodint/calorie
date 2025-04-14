import asyncio
from app import app
import streamlit as st
from data.result import Result



async def main():
    App = await app()
    if not App.stato:
        return st.error(App.errore)
    
if __name__ == "__main__":
    asyncio.run(main=main())