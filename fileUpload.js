const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileInfo = document.getElementById('fileInfo');

dropZone.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropZone.classList.add('dragover');
});

dropZone.addEventListener('dragleave', () => {
    dropZone.classList.remove('dragover');
});

dropZone.addEventListener('drop', (e) => {
    e.preventDefault();
    dropZone.classList.remove('dragover');
    handleFiles(e.dataTransfer.files);
});

fileInput.addEventListener('change', (e) => {
    handleFiles(e.target.files);
    outputGraph();
});

function handleFiles(files) {
    if (files.length > 0) {
        const file = files[0];
        fileInfo.innerHTML = `<p><strong>File:</strong> ${file.name}<br><strong>Size:</strong> ${(file.size / 1024).toFixed(2)} KB</p>`;
    }
};

function outputGraph() {
    const file = fileInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
            const content = event.target.result;
            const lines = content.split('\n');
            const x = [];
            const y = [];
            
            for (let i = lines.length - 1; i >= 0; i--) {
                const data = lines[i].trim().split(/\s+/);
                if (data.length === 2) {
                    fileInfo.innerHTML += `<p>${lines[i]}</p>`;
                    try {
                        x.push(parseFloat(data[0]));
                        y.push(parseFloat(data[1]));
                    } catch (error) {
                        break;
                    }
                }
            }
        };

        reader.readAsText(file);
    }
}
