var totalScore = 0;
var prevScore = 0;

function rndScore(){
    var num = Math.floor(Math.random()*9999);
    console.log(num);
    totalScore = num;
}

function onLoad(){
    setInterval(logicLoop, 50);
    setInterval(rndScore, 5000);
}

function logicLoop(){
    console.log("tick");
    var displayWheelText = document.getElementById("displayWheelText");
    if(displayWheelText){
        if(prevScore != totalScore){
            prevScore += Math.ceil((totalScore-prevScore)/10);
        }
        var dispNum = prevScore.toString();
        if(dispNum.length < 3){
            for(let i = 1; i < 4-dispNum.length; i++){
                dispNum = "0"+dispNum;
            }
        }
        displayWheelText.innerHTML = dispNum;
    }
}