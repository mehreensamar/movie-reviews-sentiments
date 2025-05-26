import gradio as gr
import joblib

# Load saved model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_sentiment(review):
    review_vector = vectorizer.transform([review])
    prediction = model.predict(review_vector)
    return "Positive" if prediction[0] == 1 else "Negative"

iface = gr.Interface(
    fn=predict_sentiment,
    inputs=gr.Textbox(lines=4, placeholder="Enter a movie review..."),
    outputs="text",
    title="Movie Review Sentiment Analyzer",
    description="Enter a movie review and get the sentiment prediction."
)

iface.launch()

