document.getElementById("demo").innerHTML = "Hello JavaScript";
var carName = "Volvo";

function saveToFile(){
    const textInput = document.getElementById("textInput").ariaValueMax;

    fetch("saveAndRetrieve.php", {
        method: "POST",
        body: JSON.stringify({data: textInput}),
        headers: {
            "Content-Type": "application/json",
        },
    })
    .then((response) => response.json())
    .then((data) => {
        if(data.success) {
            document.getElementById("")
            /*alert("Data saved to the file successfully.");*/
        } else{
            alert("Error saving data to the file.");
        }
    });
}