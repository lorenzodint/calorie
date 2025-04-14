import streamlit as st
import asyncio
from data.result import Result
from config.pagine import Pagine

async def config_session():
    try:
        session = st.session_state
        
        session.setdefault("page", Pagine.HOME.value)
        session.setdefault("risposta", None)
        session.setdefault("camera_on", False)
        session.setdefault("camera_front", False)
        
        
        return Result()
    except:
        return Result(stato=False, errore="Errore configurazioni sessioni")
    
    
    