from flask import Blueprint, render_template, request
import os
from flask import jsonify
from app.pdf_utils import extract_text
from app.rag import split_text, create_vectorstore, ask_pdf
from flask import redirect, url_for
main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/upload", methods=["POST"])
def upload():

    pdf = request.files["pdf"]

    if pdf.filename == "":
        return "No seleccionaste ningún PDF"

    os.makedirs("uploads", exist_ok=True)

    pdf_path = os.path.join("uploads", pdf.filename)

    pdf.save(pdf_path)

    text = extract_text(pdf_path)

    chunks = split_text(text)

    create_vectorstore(chunks)

    return redirect(url_for("main.index"))

@main.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data["question"]

    answer = ask_pdf(question)

    return jsonify({
        "answer": answer
    })