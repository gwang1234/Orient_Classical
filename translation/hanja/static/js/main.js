function uploadPDF() {
    const pdf = document.getElementById('pdf-input');
    const checkbox1 = document.getElementById('checkbox1').checked;
    const checkbox2 = document.getElementById('checkbox2').checked;

    let formdata = new FormData();
    formdata.append('pdf',pdf.files[0])
    formdata.append('checkbox1', "t")
    formdata.append('checkbox2', checkbox2 ? "t" : "f")

    // FormData 내용 확인
    for (let pair of formdata.entries()) {
        console.log(pair[0], pair[1]);
    }

    fetch ("/upload-pdf/", {
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