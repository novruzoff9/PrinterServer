# 🖨️ PrinterServer - Web Çap Xidməti

**PrinterServer** - istənilən faylı (PDF, JPG, PNG və s.) brauzerdən birbaşa çap etmək üçün hazırlanmış sadə və effektiv web tətbiqidir.

## 📋 Xüsusiyyətlər

### ✨ Əsas Funksiyalar
- 📄 **PDF fayllarının çapı** - Birbaşa PDF çapı
- 🖼️ **Şəkil fayllarının çapı** - JPG, JPEG, PNG fayllar avtomatik PDF-ə çevrilir
- 🔢 **Çap sayının seçilməsi** - istənilən sayda nüsxə çap etmək
- 🎨 **Rəng rejimi seçimi** - Ağ-qara və ya rəngli çap
- 📱 **Responsive dizayn** - Bütün cihazlarda rahat istifadə
- ⚡ **Sürətli yükləmə** - Fayllar avtomatik `jobs/` qovluğuna yüklənir

### 🎯 İstifadə Sahələri
- **Ofis mühiti** - Sənədlərin sürətli çapı
- **Ev istifadəsi** - Şəkillərin və sənədlərin çapı  
- **Kafe/İnternet klublar** - Müştərilər üçün çap xidməti
- **Məktəb/Universitet** - Tələbələr üçün çap sistemi
- **Uzaqdan çap** - Şəbəkə üzərindən çap əmrləri

## 🏗️ Sistem Arxitekturası

```
PrinterServer/
├── app.py              # Əsas Flask tətbiqi
├── templates/          
│   └── index.html      # Web interfeysi
├── static/
│   ├── style.css       # Stilləşdirmə
│   └── main.js         # JavaScript funksiyaları
├── jobs/               # Çap tarixçəsi
├── requirements.txt    # Python dependencies
└── README.md          # Bu sənəd
```

### 🔧 Texniki Təfərrüatlar

**Backend (Flask):**
- `app.py` - Əsas server tətbiqi
- Port: `5002` (bütün IP ünvanlarında)
- Fayllar `jobs/` qovluğunda saxlanılır
- PowerShell ilə səssiz çap əmrləri

**Frontend:**
- Modern HTML5/CSS3/JavaScript
- Responsive dizayn
- Real-time status yenilənmələri

## 📦 Tələb Olunan Kitabxanalar

### Python Dependencies

```bash
pip install flask pillow pywin32
```

**Ətraflı kitabxana məlumatları:**

| Kitabxana | Versiya | Məqsəd |
|-----------|---------|---------|
| `Flask` | ≥2.0.0 | Web server və routing |
| `Pillow (PIL)` | ≥8.0.0 | Şəkil fayllarını PDF-ə çevirmək || `pywin32` | ≥227 | Windows printer API dəstəyi |
### Sistem Tələbləri

- **Python:** 3.7+ (tövsiyə: 3.9+)
- **OS:** Windows 10/11 (PowerShell dəstəyi)
- **Printer:** Windows printer driver quraşdırılmış

## 🚀 Quraşdırma və İstifadə

### 1️⃣ Layihəni Endirin
```bash
git clone https://github.com/novruzoff9/PrinterServer.git
cd PrinterServer
```

### 2️⃣ Kitabxanaları Quraşdırın
```bash
pip install -r requirements.txt
```

> **Qeyd:** Manual quraşdırmaq istəsəniz:
```bash
pip install flask pillow pywin32
```

### 3️⃣ Serveri İşə Salın
```bash
python app.py
```

### 4️⃣ Brauzerdə Açın
```
http://localhost:5002
```

**Şəbəkədən giriş üçün:**
```
http://[kompüterin-ip-adresi]:5002
```

## 💻 İstifadə Təlimatı

### Addım-addım Çap Prosesi:

1. **Fayl seçin** 📁
   - "Faylı seçmək üçün kliklə" düyməsinə basın
   - PDF, JPG, JPEG, PNG və s. formatlarını seçə bilərsiniz

2. **Çap sayını təyin edin** 🔢
   - `+` və `-` düymələri ilə sayı dəyişin
   - Minimum 1 ədəd çap edə bilərsiniz
   - Default: 1 ədəd

3. **Rəng rejimini seçin** 🎨
   - **Ağ-qara:** Ağ-qara (default)
   - **Rəngli:** Tam rəngli çap

4. **Çap edin** 🖨️
   - "Çap et" düyməsinə basın
   - Status mesajını gözləyin

## ⚙️ Konfiqurasiya

### Port Dəyişdirmək
```python
# app.py faylında
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=False)  # Port-u dəyişin
```

### Debug Rejimi
```python
app.run(host="0.0.0.0", port=5002, debug=True)  # Development üçün
```

### Temp Qovluq Dəyişdirmək
```python
# app.py faylında
UPLOAD_FOLDER = "C:/CustomPath"  # Öz yolunuzu təyin edin
```

## 🔍 Troubleshooting

### Ümumi Problemlər:

**❌ "Fayl tapılmadı" xətası**
- Faylın seçildiyindən əmin olun
- Dəstəklənən formatda olduğunu yoxlayın

**❌ Çap işləmir**
- Printer-in qoşulu və hazır olduğunu yoxlayın
- Windows-da default printer təyin edin
- Printer driver-lərini yoxlayın

**❌ Port məşğuldur**
- Başqa tətbiq 5002 portunu istifadə edirsə, portu dəyişin
- Firewall ayarlarını yoxlayın

**❌ Şəkil PDF-ə çevrilmir**
- PIL/Pillow kitabxanasının quraşdırıldığını yoxlayın
- Şəkil faylının korrupted olmadığını yoxlayın

### Debug Məsləhətləri:

```bash
# Detallı error log-ları üçün:
python app.py  # Terminal açıq saxlayın

# Port-un boş olub-olmadığını yoxlamaq:
netstat -an | findstr :5002
```

## 🔧 İnkişaf

### Lokal İnkişaf:
```bash
# Virtual environment yaradın
python -m venv venv
venv\Scripts\activate

# Dependencies quraşdırın
pip install flask pillow pywin32

# Development server işə salın
python app.py
```

## 📞 Dəstək

**Problemlərinizi paylaşın:**
- GitHub Issues açın
- Email: yaghmur.novruzlu@gmail.com
- Linkedin: [Yaghmur Novruzlu](https://www.linkedin.com/in/yaghmur-novruzlu-50779a21a/)

---

**⭐ Proyekti bəyəndinizsə, star verməyi unutmayın!**
