document.getElementById('predict-button').addEventListener('click', () => {
    const gender = document.getElementById('gender').value;
    const age = document.getElementById('age').value;
    const annualIncome = document.getElementById('annual_income').value;
    
    fetch('/predict/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "gender": gender,
            "age": parseInt(age),
            "annual_income": parseInt(annualIncome)
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.prediction !== undefined) {
            // Display the prediction result
            document.getElementById('prediction-result').textContent = data.prediction.toFixed(2);
        } else if (data && data.error) {
            // Display the error message to the user
            document.getElementById('prediction-result').textContent = "Error: " + data.error;
        } else {
            console.error('Invalid response from the server.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Display the error message to the user
        document.getElementById('prediction-result').textContent = "Error: " + error.message;
    });
});
