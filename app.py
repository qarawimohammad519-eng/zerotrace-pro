import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="ZEROTRACE Builder", layout="wide")
st.title("🚀 ZEROTRACE AI Builder")

# إدخال المفتاح
api_key = st.sidebar.text_input("ضع مفتاح Google Gemini هنا:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # نستخدم نسخة مستقرة ومحدثة
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_input = st.text_area("اشرح لي الموقع الذي تريده:")
        if st.button("أطلق الموقع الآن"):
            with st.spinner('جاري البناء...'):
                response = model.generate_content(f"اكتب كود HTML كامل لموقع عن: {user_input}")
                st.markdown("### كود موقعك جاهز:")
                st.code(response.text, language='html')
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
else:
    st.info("💡 احصل على مفتاح مجاني من aistudio.google.com")
