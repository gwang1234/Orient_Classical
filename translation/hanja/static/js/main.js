function check() {
    const checkbox1 = document.getElementById('checkbox1').checked;
    const checkbox2 = document.getElementById('checkbox2').checked;

    let formdata = new FormData();
    formdata.append('checkbox1', checkbox1 ? "t" : "f")
    formdata.append('checkbox2', checkbox2 ? "t" : "f")

    fetch ("/index/", {
        method: "POST",
        body: formdata,
    })
    .then(response => {
    if (!response.ok) {
        throw new Error(`서버 오류: ${response.status}`);
    }
    return response.json();
    })
    .catch(error => console.error('Error: ',error))
}

function uploadPDF() {
    const pdf = document.getElementById('pdf-input');
    const checkbox1 = document.getElementById('checkbox1').checked;
    const checkbox2 = document.getElementById('checkbox2').checked;

    const formData = new FormData();
    formData.append('pdf', pdf.files[0]);  // 파일 데이터
    
    const jsonData = JSON.stringify({
        checkbox1: checkbox1 ? "t" : "f",
        checkbox2: checkbox2 ? "t" : "f"
    });
    
    fetch("/upload-pdf/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
    
}