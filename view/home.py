import streamlit as st
import asyncio
from data.result import Result
from PIL import Image
import utils.functions as func
import utils.ai as ai
from config.pagine import Pagine
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration


async def mostra():
    try:
        session = st.session_state
        
        

        st.header("Analizza cibo e calorie")
        st.write(
            "Carica una foto di un cibo per analizzarlo e ottenere informazioni sulle calorie.")

        t1, t2 = st.tabs(['Caricamento', "Fotocamera"])

        with t1:
            # st.write("carica foto")

            carica_foto = st.file_uploader(
                "Scegli un'immagine di cibo...",
                type=["jpg", "jpeg", "png"],
                accept_multiple_files=False
            )
            if carica_foto is not None:
                image = Image.open(carica_foto)
                # st.image(image, caption="Foto caricata",
                #          use_container_width=True)

                if st.button("Analizza questo cibo"):
                    with st.spinner("Analisi dell'immagine in corso...", show_time=True):
                        carica_foto.seek(0)

                        img_base64 = await func.encoded_image(carica_foto)
                        if not img_base64.stato:
                            return st.error(img_base64.errore)

                        analisi = await ai.anlisi_ai(img_base64.risultato)
                        if not analisi.stato:
                            return st.error(analisi.errore)
                        session.risposta = analisi.risultato
                        session.page = Pagine.ANALISI.value
                        st.rerun()



        with t2:
            st.write("Scatta una foto")
            
            # # Pulsante per attivare/disattivare la fotocamera
            # if st.button("📸 " + ("Spegni" if session.camera_on else "Accendi") + " Fotocamera"):
            #     session.camera_on = not session.camera_on
            #     st.rerun()

            # if session.camera_on:
            #     # Pulsante per cambiare tipo di fotocamera
            #     if st.button("🔄 Cambia Fotocamera " + ("Posteriore" if session.camera_front else "Frontale")):
            #         session.camera_front = not session.camera_front
            #         st.rerun()

            #     # Configurazione WebRTC
            #     rtc_configuration = RTCConfiguration(
            #         {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
            #     )

            #     # Stream della fotocamera
            #     webrtc_ctx = webrtc_streamer(
            #         key="camera",
            #         mode=WebRtcMode.SENDRECV,
            #         rtc_configuration=rtc_configuration,
            #         video_frame_callback=None,
            #         media_stream_constraints={
            #             "video": {
            #                 "facingMode": "user" if session.camera_front else "environment"
            #             },
            #             "audio": False
            #         }
            #     )

            #     # Pulsante per scattare la foto
            #     if webrtc_ctx.state.playing and st.button("📸 Scatta Foto"):
            #         if webrtc_ctx.video_receiver:
            #             # Qui andrà la logica per catturare il frame
            #             # e processare l'immagine
            #             st.success("Foto scattata!")
            #             # Esempio:
            #             # frame = webrtc_ctx.video_receiver.get_frame()
            #             # image = frame.to_ndarray(format="bgr24")
            #             # ... processo l'immagine ...




            if st.button("Attiva/Disattiva fotocamera"):
                session.camera_on = not session.camera_on
                st.rerun()

            

            picture = st.camera_input("Scatta foto", 
                                    disabled=not session.camera_on,
                                    key="camera_" + ("front" if session.camera_front else "back"))

            if picture:
                st.image(picture)
                if st.button("Analizza questo cibo"):
                    with st.spinner("Analisi dell'immagine in corso...", show_time=True):
                        img_base64 = await func.encoded_image(picture)
                        if not img_base64.stato:
                            return st.error(img_base64.errore)

                        analisi = await ai.anlisi_ai(img_base64.risultato)
                        if not analisi.stato:
                            return st.error(analisi.errore)
                        session.risposta = analisi.risultato
                        session.page = Pagine.ANALISI.value
                        session.camera_on = False
                        st.rerun()




        return Result()
    except Exception as e:
        return Result(stato=False, errore=f"Errore visualizzazione pagina Home\n\n{e}")
