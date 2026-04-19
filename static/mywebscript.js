function RunSentimentAnalysis() {
  const text = document.getElementById("textToAnalyse").value;
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("system_response").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "/emotionDetector?textToAnalyse=" + encodeURIComponent(text), true);
  xhttp.send();
}
