import streamlit as st

# Styling
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 70px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        border: none;
    }
    .anzeige {
        background-color: #2d2d2d;
        color: white;
        font-size: 36px;
        text-align: right;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧮 Taschenrechner")

# Zustand initialisieren
if "eingabe" not in st.session_state:
    st.session_state.eingabe = ""

# Anzeige
st.markdown(f'<div class="anzeige">{st.session_state.eingabe if st.session_state.eingabe else "0"}</div>', unsafe_allow_html=True)

# Button-Klick Funktion
def klick(wert):
    aktuell = st.session_state.eingabe

    if wert == "C":
        st.session_state.eingabe = ""

    elif wert == "⌫":
        st.session_state.eingabe = aktuell[:-1]

    elif wert == "=":
        try:
            ausdruck = aktuell.replace("÷", "/").replace("×", "*")
            ergebnis = eval(ausdruck)
            if ergebnis == int(ergebnis):
                st.session_state.eingabe = str(int(ergebnis))
            else:
                st.session_state.eingabe = str(round(ergebnis, 10))
        except:
            st.session_state.eingabe = "❌ Fehler"

    else:
        if aktuell == "❌ Fehler":
            st.session_state.eingabe = ""
        st.session_state.eingabe += wert

# Button-Layout
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "⌫"]
]

# Buttons erstellen
for zeile in buttons:
    cols = st.columns(len(zeile))
    for i, wert in enumerate(zeile):
        if cols[i].button(wert, use_container_width=True, on_click=klick, args=(wert,)):
            pass
