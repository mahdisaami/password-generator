import streamlit as st
from generator import RandomPasswordGenerator, PinPassword, MemorablePasswordGenerator

st.set_page_config(page_title="Password Generator", page_icon="🔐")

st.title("Password Generator")

generator_type = st.sidebar.selectbox("Generator type", ["Random", "PIN", "Memorable"])

if generator_type == "Random":
    length = st.sidebar.slider("Length", min_value=1, max_value=30, value=12)
    digits = st.sidebar.toggle("Include digits", value=True)
    symbols = st.sidebar.toggle("Include symbols", value=True)
    gen = RandomPasswordGenerator(allowed_digits=digits, allowed_symbols=symbols, length=length)

elif generator_type == "PIN":
    length = st.sidebar.slider("PIN length", min_value=1, max_value=32, value=4)
    gen = PinPassword(length)

else:  # Memorable
    length = st.sidebar.slider("Number of words", min_value=1, max_value=8, value=3)
    separator = st.sidebar.text_input("Separator", value="-")
    uppercase = st.sidebar.toggle("Uppercase", value=False)
    gen = MemorablePasswordGenerator(seperator=separator, length=length, uppercase=uppercase)

count = st.sidebar.number_input("How many to generate", min_value=1, max_value=50, value=1)

if st.button("Generate"):
    results = [gen.generate_password() for _ in range(count)]
    if count == 1:
        st.code(results[0])
        st.download_button("Download password", results[0], file_name="password.txt")
    else:
        st.code("\n".join(results))
        st.download_button("Download passwords", "\n".join(results), file_name="passwords.txt")

st.markdown("---")
st.markdown("Built with <3 — select options in the sidebar and press Generate.")

