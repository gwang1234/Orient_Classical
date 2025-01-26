function uploadPDF() {
    const pdf = document.getElementById('pdf-input');
    let formdata = new FormData();
    formdata.append('pdf',pdf.files[0])

    fetch ("/upload-pdf/", {
        method: "POST",
        body: formdata,
        headers: {

        }
    })
    .catch(error => console.error('Error: ',error))
}