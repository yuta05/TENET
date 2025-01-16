import sys
import os
from dotenv import load_dotenv
from IPython.display import Image, display

# プロジェクトのルートディレクトリを sys.path に追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

# .env ファイルを読み込む
load_dotenv(os.path.join(os.path.dirname(__file__), '../../..', '.env'))

from app.services.cs_agents.agent import part_4_graph  # Import part_4_graph from graph.py

try:
    graph_image = part_4_graph.get_graph(xray=True).draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(graph_image)
    display(Image("graph.png"))
except Exception as e:
    print(f"An error occurred: {e}")