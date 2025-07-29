# ✍️ Signature Matching Web Service

This is a lightweight, local-first Python web app for comparing two signature images. It uses pretrained vision models to generate embeddings and evaluates similarity via cosine distance.

Perfect for quick offline testing, demos, or integration into larger identity verification systems.

---

## 🚀 Features

- Upload and compare two handwritten signature images via browser.
- Returns a match score with intuitive labels like:
  - ✅ Exact Match
  - 🟢 High Match
  - 🟡 Moderate Match
  - 🟠 Weak Match
  - 🔴 No Match
- Embedding-based similarity using pretrained **MobileNetV2** via `timm`.
- Clean UI with side-by-side preview of uploaded signatures.
- Fully self-contained – no external LLMs or APIs needed.
- Can be Dockerized and shipped to any plain Linux VM.

---

## 🧰 Tech Stack

| Component       | Description                                |
|-----------------|--------------------------------------------|
| **Flask**       | Web framework for serving UI and backend   |
| **PyTorch**     | ML framework powering the vision model     |
| **timm**        | PyTorch Image Models (pretrained MobileNet)|
| **OpenCV**      | Image loading and preprocessing             |
| **scikit-learn**| Cosine similarity computation               |
| **Docker**      | Containerization for cross-platform testing |

---

## 🖼️ How It Works

1. Each signature image is passed through a **MobileNetV2 encoder**.
2. This generates a **128-dimensional embedding vector**.
3. Embeddings are compared using **cosine similarity**.
4. A percent match is computed and labeled intuitively.

---

## 📦 Setup (Non-Docker)

### 1. Clone and Install
```bash
git clone https://github.com/your-user/signature-matcher.git
cd signature-matcher

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
