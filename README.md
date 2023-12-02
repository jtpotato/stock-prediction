![](https://project-cards.jtpotatodev.workers.dev/?project=jtpotato/stock-prediction&started=1%20Dec%202023&codename=Otway)

An experiment to see how well Facebook's Prophet can be used to predict stocks.

Note: **under no circumstances should this tool be the sole basis for financial decisions. As outlined in the license, this software or its creators/maintainers are not liable for any losses.**

# Setup
```bash
git clone https://github.com/jtpotato/stock-prediction --depth=1 # Clone the repository. This is the easiest way to download all of the files required.

cd stock-prediction

# Install Dependencies:
python3 -m pip install -r requirements.txt
# OR
python -m pip install -r requirements.txt
# OR
pip install -r requirements.txt
```
# Usage
1. Run `src/main.py`
```bash
python3 src/main.py
```
2. Open the URL in your browser. (Most likely `http://127.0.0.1:7860`)
![image](https://github.com/jtpotato/stock-prediction/assets/58995538/ccdbd97b-686e-476d-8b18-06cffb9a193f)

3. Create a list of stocks to predict for
![image](https://github.com/jtpotato/stock-prediction/assets/58995538/42c4da81-c256-4b1b-8172-c62d46832953)

4. Hit **Download**
![image](https://github.com/jtpotato/stock-prediction/assets/58995538/c5f6c4ff-37b0-4d7d-b119-175f7159ae85)

5. Hit **Predict**
![image](https://github.com/jtpotato/stock-prediction/assets/58995538/db83486d-9f41-4c6f-a2c6-a0aa8e55d82c)

# Tech Stack
- Facebook/Prophet
- Gradio
- yfinance
