function increaseCount() {
    const input = document.getElementById('printCount');
    input.value = parseInt(input.value) + 1;
}

function decreaseCount() {
    const input = document.getElementById('printCount');
    const currentValue = parseInt(input.value);
    if (currentValue > 1) {
        input.value = currentValue - 1;
    }
}

function sendFile() {
    const fileInput = document.getElementById('fileInput');
    const printCount = document.getElementById('printCount').value;
    const colorMode = document.querySelector('input[name="colorMode"]:checked').value;
    const statusEl = document.getElementById('status');

    if (!fileInput.files[0]) {
        statusEl.textContent = 'Zəhmət olmasa fayl seçin!';
        statusEl.className = 'error';
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    formData.append('count', printCount);
    formData.append('color', colorMode);

    statusEl.textContent = 'Fayl yüklənir və çap edilir...';
    statusEl.className = '';

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        statusEl.textContent = data;
        statusEl.className = 'success';
        // Reset form after successful upload
        fileInput.value = '';
        document.getElementById('printCount').value = '1';
        document.querySelector('input[name="colorMode"][value="bw"]').checked = true;
        document.querySelector('.custom-file-upload').textContent = 'Faylı seçmək üçün kliklə';
    })
    .catch(error => {
        statusEl.textContent = 'Xəta baş verdi: ' + error;
        statusEl.className = 'error';
    });
}

// File input change event to show selected file name
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fileInput');
    const label = document.querySelector('.custom-file-upload');
    
    fileInput.addEventListener('change', function() {
        if (this.files[0]) {
            label.textContent = 'Seçildi: ' + this.files[0].name;
        } else {
            label.textContent = 'Faylı seçmək üçün kliklə';
        }
    });
});
