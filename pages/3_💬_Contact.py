import streamlit as st


black_text = '<h1 style="color:black;">Get In Touch With Me!</h1>'


st.markdown(black_text, unsafe_allow_html=True)


st.write("""
Jika Anda mengalami masalah atau memiliki pertanyaan lebih lanjut, jangan ragu untuk mengisi form dibawah, saya akan menghubungi Anda.


Semua umpan balik Anda sangat dihargai. Terima kasih! 👥
""")


contact_form = """
<form action="https://formsubmit.co/rhevaanindyaw@gmail.com" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" placeholder="Your email" required>
<textarea name="message" placeholder="Your message here"></textarea>
<button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
