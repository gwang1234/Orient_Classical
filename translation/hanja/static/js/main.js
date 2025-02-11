function uploadPDF() {
    const pdf = document.getElementById('pdf-input');

    const formData = new FormData();
    formData.append('pdf', pdf.files[0]);  // 파일 데이터
    
    fetch("/upload-pdf/", {
        method: "POST",
        body: formData
    })
    // .then(response => response.blob())  // 응답을 Blob 형태로 받음
    // .then(blob => {
    //     const url = window.URL.createObjectURL(blob);
    //     const a = document.createElement('a');
    //     a.href = url;
    //     a.download = 'download.pdf';  // 다운로드할 파일 이름
    //     document.body.appendChild(a);
    //     a.click();
    //     a.remove();
    // })
    .catch(error => console.error('Error:', error));
    
}