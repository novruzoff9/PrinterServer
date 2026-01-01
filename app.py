from flask import Flask, render_template, request, send_from_directory
import os
import subprocess
from PIL import Image
import win32print

app = Flask(__name__, static_folder='static', template_folder='templates')

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'jobs')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def is_image(filename):
    ext = filename.lower()
    return ext.endswith(".jpg") or ext.endswith(".jpeg") or ext.endswith(".png")


def convert_image_to_pdf(image_path, color_mode="bw"):
    pdf_path = image_path + ".pdf"
    image = Image.open(image_path)
    if color_mode == "bw":
        image = image.convert("L")
        image = image.convert("RGB")
    else:
        image = image.convert("RGB")
    
    image.save(pdf_path, "PDF", quality=95)
    return pdf_path


def print_file(filepath, count=1, color_mode="bw"):
    try:
        printer_name = win32print.GetDefaultPrinter()
        printer_handle = win32print.OpenPrinter(printer_name)
        for _ in range(int(count)):
            if color_mode == "bw":
                subprocess.run([
                    "powershell",
                    "-Command",
                    f'& "C:\\Program Files\\SumatraPDF\\SumatraPDF.exe" -print-to-default -print-settings "monochrome" -exit-when-done "{filepath}"'
                ], shell=True, capture_output=True)
                
                if subprocess.run(["where", "SumatraPDF.exe"], capture_output=True).returncode != 0:
                    subprocess.run([
                        "powershell",
                        "-Command",
                        f"Start-Process -FilePath '{filepath}' -Verb Print -WindowStyle Hidden"
                    ], shell=True)
            else:
                subprocess.run([
                    "powershell",
                    "-Command", 
                    f"Start-Process -FilePath '{filepath}' -Verb Print -WindowStyle Hidden"
                ], shell=True)
        
        win32print.ClosePrinter(printer_handle)
        
    except Exception as e:
        for _ in range(int(count)):
            subprocess.run([
                "powershell",
                "-Command",
                f"Start-Process -FilePath '{filepath}' -Verb Print -WindowStyle Hidden"
            ], shell=True)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "Fayl tapılmadı", 400

    files = request.files.getlist('file')

    if not files or files[0].filename == '':
        return "Fayl seçilməyib", 400

    print_count = request.form.get('count', '1')
    color_mode = request.form.get('color', 'bw')

    processed_files = []
    errors = []

    for file in files:
        if file.filename == '':
            continue

        try:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            if is_image(file.filename):
                try:
                    pdf_path = convert_image_to_pdf(filepath, color_mode)
                    filepath = pdf_path
                except Exception as e:
                    errors.append(f"{file.filename}: PDF çevirmə xətası - {str(e)}")
                    continue

            try:
                print_file(filepath, print_count, color_mode)
                processed_files.append(file.filename)
            except Exception as e:
                errors.append(f"{file.filename}: Çap xətası - {str(e)}")
        except Exception as e:
            errors.append(f"{file.filename}: Ümumi xəta - {str(e)}")

    color_text = "ağ-qara" if color_mode == "bw" else "rəngli"
    
    if processed_files and not errors:
        return f"{len(processed_files)} fayl {print_count} ədəd {color_text} çap edildi: {', '.join(processed_files)}", 200
    elif processed_files and errors:
        return f"{len(processed_files)} fayl çap edildi. Xətalar: {'; '.join(errors)}", 207
    else:
        return f"Çap zamanı xətalar baş verdi: {'; '.join(errors)}", 500


@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=False)