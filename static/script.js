function search(){

    let input = document.getElementById("upload")

    if(input.files.length === 0){
        alert("Please choose an image")
        return
    }

    let file = input.files[0]

    let formData = new FormData()

    formData.append("image", file)

    fetch("/search", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {

        let results = document.getElementById("results")

        results.innerHTML = ""

        data.forEach(item => {

            let div = document.createElement("div")

            div.innerHTML = `
                <img src="/dataset/${item.image}" width="200">
                <p>Score: ${item.score.toFixed(3)}</p>
            `

            results.appendChild(div)

        })

    })
}