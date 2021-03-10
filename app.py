import streamlit as st

def tokenize(text):
    tokens = text.split()
    return tokens

def run():
    st.title("Hello Streamlit")
    st.header("This is a simple app")
    st.image('./hello.jpg')
    text = st.text_area("Enter your text here")
    # output = ""
    if st.button("Calculate"):
        output = tokenize(text)
        st.success(f"{output}")
        # st.balloons()

if __name__=="__main__":
    run()