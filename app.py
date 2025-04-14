import asyncio
import streamlit as st
from data.result import Result
from config.session import config_session
import utils.functions as func


async def app():
    try:
        session = st.session_state
        st.set_page_config(layout="centered")

        hide_github_icon = """
#GithubIcon {
  visibility: hidden;
}
"""
        st.markdown(hide_github_icon, unsafe_allow_html=True)

        configurazione_session = await config_session()
        if not configurazione_session.stato:
            return st.error(configurazione_session.errore)

        # st.title("APP")

        router = await func.router_pagine()
        if not router.stato:
            return st.error(router.errore)

        # st.write(session)

        return Result()
    except Exception as e:
        return Result(stato=False, errore="Errore caricamento App")
