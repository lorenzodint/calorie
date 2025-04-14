import streamlit as st
import asyncio
from data.result import Result
from config.pagine import Pagine


async def mostra():
    try:
        session = st.session_state
        st.header("Analisi Cibo")

        if session.risposta is not None:
            c1, c2 = st.columns([1, 1], border=True)
            with c1:
                st.badge("Cibo:", color="blue")
                st.write(session.risposta.output_parsed.cibo)
            with c2:
                st.badge("Info:", color="blue")
                st.write(session.risposta.output_parsed.info)
            with st.container(border=True):
                st.badge("Calorie:", color="orange")
                st.write(session.risposta.output_parsed.calorie)
            c1, c2 = st.columns([1, 1], border=True)
            with c1:
                st.badge("Consigli:", color="green")
                st.write(session.risposta.output_parsed.consigli)
            with c2:
                st.badge("Rischi:", color="red")
                st.write(session.risposta.output_parsed.rischi)
        if st.button("Analizza altro cibo"):
            session.page = Pagine.HOME.value
            st.rerun()
        
        return Result()
    except Exception as e:
        return Result(stato=False, errore=f"Errore visualizzazione pagina analisi cibo")
