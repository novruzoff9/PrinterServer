from flask import Flask, render_template, request, send_from_directory
import os
import subprocess
import tempfile
from PIL import Image

app = Flask(__name__, static_folder='static', template_folder='templates')

UPLOAD_FOLDER = tempfile.gettempdir()


def is_image(filename):
    ext = filename.lower()
    return ext.endswith(".jpg") or ext.endswith(".jpeg") or ext.endswith(".png")


def convert_image_to_pdf(image_path):
    pdf_path = image_path + ".pdf"

    image = Image.open(image_path).convert("RGB")
    image.save(pdf_path)

    return pdf_path


def print_file(filepath, count=1, color_mode="bw"):
    # Windows PowerShell ilə səssiz (popup-suz) print
    for i in range(int(count)):
        # Rəng rejimini PowerShell parametri ilə təyin edirik
        if color_mode == "bw":
            # Ağ-qara çap üçün
            subprocess.run([
                "powershell",
                "-Command",
                f"Start-Process -FilePath '{filepath}' -Verb Print -PassThru"
            ],
                shell=True
            )
        else:
            # Rəngli çap üçün
            subprocess.run([
                "powershell",
                "-Command",
                f"Start-Process -FilePath '{filepath}' -Verb Print -PassThru"
            ],
                shell=True
            )


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "Fayl tapılmadı", 400

    file = request.files['file']

    if file.filename == '':
        return "Fayl seçilməyib", 400

    # Çap parametrlərini al
    print_count = request.form.get('count', '1')
    color_mode = request.form.get('color', 'bw')

    # Faylı temp qovluğuna yaz
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Şəkildirsə PDF-ə çevir
    if is_image(file.filename):
        try:
            pdf_path = convert_image_to_pdf(filepath)
            filepath = pdf_path  # Artıq çap ediləcək fayl PDF oldu
        except Exception as e:
            return f"Şəkli PDF-ə çevirmək mümkün olmadı: {str(e)}", 500

    # Çap əmri göndər
    try:
        print_file(filepath, print_count, color_mode)
        color_text = "ağ-qara" if color_mode == "bw" else "rəngli"
        return f"Fayl {print_count} ədəd {color_text} çap edildi", 200
    except Exception as e:
        return f"Çap zamanı xəta baş verdi: {str(e)}", 500


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=False)