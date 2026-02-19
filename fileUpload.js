

// TODO: #3 Document script

const dropZone = document.getElementById('dropZone');
const fileInput = document.getElementById('fileInput');
const fileInfo = document.getElementById('fileInfo');
const graphZone = document.getElementById('graphZone');

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
    getData();
    outputGraph();
});

// TODO: #2 Add error handling for file reading and parsing

function handleFiles(files) {
    if (files.length > 0) {
        const file = files[0];
        fileInfo.innerHTML = `<p><strong>File:</strong> ${file.name}<br><strong>Size:</strong> ${(file.size / 1024).toFixed(2)} KB</p>`;
    }
};

function getData() {
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

// TODO: #4 FIx output of graph after file is read and parsed

function outputGraph() {
    Plotly.newPlot(graphZone, [{
        x: x,
        y: y }], { 
        margin: { t: 0 } }, {showSendToCloud:true}
    );
    
    console.log( Plotly.BUILD );
};
