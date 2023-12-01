import gradio as gr

from download import download_tickers
from predict import predict_all

with gr.Blocks() as demo:
    tickers = gr.Textbox(label="Enter tickers separated by newline")
    download_status = gr.Textbox(label="Download status")
    download_btn = gr.Button("Download")
    download_btn.click(fn=download_tickers, inputs=tickers, outputs=download_status)
    prediction_results = gr.Gallery()
    predict_btn = gr.Button("Predict")
    predict_btn.click(fn=predict_all, outputs=prediction_results)

demo.launch()