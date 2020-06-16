function analysisInitializer() {


    var keyword = document.getElementById("keyword")
    var number = document.getElementById("number")
    var track = document.getElementById("submit-btn")
    console.log("hello")
    var keyval = keyword.value
    var numval = number.value
    if (keyval == "" || numval == "") {
        alert("Keyword or Number of tweets cannot be empty!")
    }
    else {
        track.disabled = true
        track.value = "Loading..."
        eel.main(keyval, numval)(function (data) {
            console.log(data)
            pieData = [data.pos_polarity.length, data.neg_polarity.length, data.neu_polarity]
            lineData = data.polarity
            barData = [data.pos_polarity.length, data.neg_polarity.length, data.neu_polarity]
            visualize(keyval, numval, pieData, lineData, barData)
            track.disabled = false
            track.value = "Track"
        })
    }
    keyword.value = ""
    number.value = ""
}

let pieChart = 0
let lineChart = 0
let barChart = 0

function visualize(keyword, number, pieData, lineData, barData) {


    let pieCanvas = document.getElementById("pie-chart").getContext("2d");
    let lineCanvas = document.getElementById("line-chart").getContext("2d");
    let barCanvas = document.getElementById("bar-chart").getContext("2d");


    if (pieChart instanceof Chart && lineChart instanceof Chart && barChart instanceof Chart) {
        pieChart.clear()
        pieChart.destroy()
        lineChart.clear()
        lineChart.destroy()
        barChart.clear()
        barChart.destroy()
    }

    pieChart = new Chart(pieCanvas, {
        type: 'pie',
        data: {
            labels: ["Positive", "Negative", "Neutral"],
            datasets: [{
                label: keyword,
                data: pieData,
                backgroundColor: ["#4A89DC", "#434A54", "#2ABA66", "#BF263C"]
            }]
        },
        options: {}
    })

    lineChart = new Chart(lineCanvas, {
        type: 'line',
        data: {
            labels: ["Positive", "Negative", "Neutral"],
            datasets: [{
                label: keyword,
                data: lineData,
                backgroundColor: ["#4A89DC", "#434A54", "#2ABA66", "#BF263C"]
            }]
        },
        options: {}
    })

    barChart = new Chart(barCanvas, {
        type: 'bar',
        data: {
            labels: ["Positive", "Negative", "Neutral"],
            datasets: [{
                label: keyword,
                data: barData,
                backgroundColor: ["#4A89DC", "#434A54", "#2ABA66", "#BF263C"]
            }]
        },
        options: {}
    })

}