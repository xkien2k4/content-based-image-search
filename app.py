import os
import cv2
import numpy as np

from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename

# ==========================
# CONFIG
# ==========================

DATASET_PATH = "dataset"
UPLOAD_FOLDER = "uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ==========================
# LOAD FEATURE DATABASE
# ==========================

print("Loading features...")

features = np.load("features.npy")
names = np.load("names.npy")

database = []

for i in range(len(names)):
    database.append({
        "name": str(names[i]),
        "feature": features[i]
    })

print("Dataset loaded:", len(database))

# ==========================
# COSINE SIMILARITY
# ==========================

def similarity(f1, f2):

    return np.dot(f1, f2) / (np.linalg.norm(f1) * np.linalg.norm(f2))

# ==========================
# ROUTES
# ==========================

@app.route("/")
def home():

    return render_template("index.html")


# Route để hiển thị ảnh dataset
@app.route("/dataset/<filename>")
def dataset_image(filename):

    return send_from_directory(DATASET_PATH, filename)


# Route tìm ảnh
@app.route("/search", methods=["POST"])
def search():

    if "image" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["image"]

    if file.filename == "":
        return jsonify({"error": "No file selected"})

    filename = secure_filename(file.filename)

    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)

    file.save(path)

    img = cv2.imread(path)

    if img is None:
        return jsonify({"error": "Invalid image"})

    from feature import extract_feature

    query_feature = extract_feature(img)

    results = []

    for item in database:

        score = similarity(query_feature, item["feature"])

        results.append({
            "image": item["name"],
            "score": float(score)
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return jsonify(results[:20])


# ==========================
# RUN SERVER
# ==========================

if __name__ == "__main__":

    app.run(debug=True)