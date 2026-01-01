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

    if (!fileInput.files || fileInput.files.length === 0) {
        statusEl.textContent = 'Zəhmət olmasa fayl seçin!';
        statusEl.className = 'error';
        return;
    }

    const formData = new FormData();
    
    for (let i = 0; i < fileInput.files.length; i++) {
        formData.append('file', fileInput.files[i]);
    }
    
    formData.append('count', printCount);
    formData.append('color', colorMode);

    const fileCount = fileInput.files.length;
    statusEl.textContent = `${fileCount} fayl yüklənir və çap edilir...`;
    statusEl.className = '';

    fetch('/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        statusEl.textContent = data;
        statusEl.className = 'success';
        fileInput.value = '';
        document.getElementById('printCount').value = '1';
        document.querySelector('input[name="colorMode"][value="bw"]').checked = true;
        document.querySelector('.custom-file-upload').textContent = 'Faylları seçmək üçün kliklə';
    })
    .catch(error => {
        statusEl.textContent = 'Xəta baş verdi: ' + error;
        statusEl.className = 'error';
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('fileInput');
    const label = document.querySelector('.custom-file-upload');
    
    fileInput.addEventListener('change', function() {
        if (this.files && this.files.length > 0) {
            if (this.files.length === 1) {
                label.textContent = 'Seçildi: ' + this.files[0].name;
            } else {
                label.textContent = `Seçildi: ${this.files.length} fayl`;
            }
        } else {
            label.textContent = 'Faylları seçmək üçün kliklə';
        }
    });
});
