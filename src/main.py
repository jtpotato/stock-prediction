import gradio as gr

from download import download_tickers
from init_file_system import initialise_filesystem
from predict import predict_all

with gr.Blocks() as demo:
    instructions_1 = gr.Markdown("# jtpotato/stock-prediction\n## Step 1: Download data for your chosen tickers.\nIt is much, much easier to do all of this at once.\n\n📈 We follow the Yahoo Finance ticker format.\n\n ⌨️ Press `Shift + Enter` for a new line.")
    tickers = gr.Textbox(label="Enter tickers separated by newline")
    download_status = gr.Textbox(label="Download status")
    download_btn = gr.Button("Download")
    download_btn.click(fn=download_tickers, inputs=tickers, outputs=download_status)
    instructions_2 = gr.Markdown("## Step 2: Predict stock prices for the next 28 days.\nLook through the charts yourself to see if the results are agreeable. `jtpotato/stock-prediction` does not have access to any news events and therefore cannot predict sudden changes in stock price.")
    prediction_results = gr.Gallery()
    predict_btn = gr.Button("Predict")
    predict_btn.click(fn=predict_all, outputs=prediction_results)
    instructions_3 = gr.Markdown("*Under no circumstances should this tool be the sole basis for financial decisions. As outlined in the license, this software or its creators/maintainers are not liable for any losses.*")

initialise_filesystem()

demo.launch()