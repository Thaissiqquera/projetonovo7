from flask import Flask, jsonify, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.linear_model import LinearRegression

# Configura Flask para servir templates e estáticos na raiz
app = Flask(
    __name__,
    template_folder='.',      # busca index.html na raiz
    static_url_path='',       # arquivos estáticos acessíveis na raiz
    static_folder='.'         # serve todos arquivos da raiz
)

@app.route('/')
def index():
    return render_template('index.html')

# ... o restante das rotas (sem alterações) ...

if __name__ == '__main__':
    app.run(debug=True)
