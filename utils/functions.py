import asyncio
import streamlit as st
from data.result import Result
from config.pagine import Pagine
import view
from PIL import Image
import base64
import io


async def router_pagine():
    try:
        session = st.session_state
        if session.page == Pagine.HOME.value:
            page = await view.home.mostra()
            if not page.stato:
                return st.error(page.errore)
            return Result()
        if session.page == Pagine.ANALISI.value:
            page = await view.analisi_cibo.mostra()
            if not page.stato:
                return st.error(page.errore)
            return Result()
    except Exception as e:
        return Result(stato=False, errore="Errore router pagine")
    
    
    
async def encoded_image(image_file):
    try:
        # Apre l'immagine con PIL
        img = Image.open(image_file)
        
        # Converti in formato JPEG o PNG (formati supportati da OpenAI)
        buffer = io.BytesIO()
        if img.format == 'PNG':
            img.save(buffer, format="PNG")
        else:
            img.save(buffer, format="JPEG", quality=95)
        
        # Codifica in base64
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        return Result(stato=True, risultato=img_str)
    except Exception as e:
        return Result(stato=False, errore=f"Errore codifica immagine: {str(e)}")
    
    