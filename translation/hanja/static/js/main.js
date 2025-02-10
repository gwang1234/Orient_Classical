function uploadPDF() {
    const pdf = document.getElementById('pdf-input');

    const formData = new FormData();
    formData.append('pdf', pdf.files[0]);  // 파일 데이터
    
    fetch("/upload-pdf/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    
}