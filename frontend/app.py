
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="SMS Shield",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ SMS Shield")
st.subheader("Intelligent SMS Spam Detection")

st.write(
    "Enter an SMS message below to check "
    "whether it is Spam or Not Spam."
)

message = st.text_area(
    "Enter your SMS message",
    placeholder="Type your message here...",
    height=150
)

if st.button("Analyze Message", type="primary"):

    if not message.strip():
        st.warning("Please enter an SMS message.")

    else:
        try:
            response = requests.post(
                API_URL,
                json={"message": message},
                timeout=10
            )

            if response.status_code == 200:
                result = response.json()

                if result["prediction"].lower() == "spam":
                    st.error("🚨 This message is SPAM")
                else:
                    st.success("✅ This message is NOT SPAM")

                st.write("Prediction:", result["prediction"])

            else:
                st.error(
                    f"API Error: {response.json().get('detail', 'Unknown error')}"
                )

        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to FastAPI backend. Start the API first.")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
