var totalScore = 0;
var prevScore = 0;

var powerScore = 0;
var prevPowerScore = 0;
var lastPowerScore = 0;
var waterScore = 0;
var prevWaterScore = 0;
var lastWaterScore = 0;

//score*cost = total cost per 24, maybe?
var cost24Power = 0.0005;
var cost24Water = 0.0009;

// helper functions should make sense
function rndScore(){
    var num = Math.floor(Math.random()*9999);
    lastPowerScore = powerScore;
    powerScore = num;
    num = Math.floor(Math.random()*9999);
    lastWaterScore = waterScore;
    waterScore = num;
    totalScore = powerScore+waterScore;
}

function onLoad(){
    setInterval(logicLoop, 50);
    setInterval(rndScore, 5000);
}

function lerpValue(newVal, oldVal, magnitude){
    if(oldVal != newVal){
        oldVal += Math.ceil((newVal-oldVal)/magnitude);
    }
    return oldVal;
}

function valToString(val, leadingZeroes){
    var newVal = val.toString();
    var returnVal = newVal;
    if(newVal.length < leadingZeroes){
        for(let i = 0; i < leadingZeroes-newVal.length; i++){
            returnVal = "0"+returnVal;
        }
    }
    return returnVal;
}

function percentDifference(oldVal, newVal){
    var diff = newVal-oldVal
    return Math.floor(diff/oldVal*100)
}

//default logic loop for updating values on the page
function logicLoop(){

    var totalScoreDisplay = document.getElementById("displayWheelText");
    var waterScoreDisplay = document.getElementById("sectionValueWater");
    var waterScorePDisplay = document.getElementById("sectionPercentValueWater");
    var powerScoreDisplay = document.getElementById("sectionValuePower");
    var powerScorePDisplay = document.getElementById("sectionPercentValuePower");

    var powerProgress = document.getElementById("progressTextPower");
    var powerProgressVal = document.getElementById("progressValuePower");
    var waterProgress = document.getElementById("progressTextWater");
    var waterProgressVal = document.getElementById("progressValueWater");

    var lowerInfo = document.getElementById("displayLowerInfo");
    var dispString;

    // updates the numbers on the top half the page
    if(prevScore != totalScore){
        prevScore = lerpValue(totalScore, prevScore, 10);
        dispString = valToString(prevScore, 3);
        totalScoreDisplay.innerHTML = dispString;
    };
    if(prevWaterScore != waterScore){
        prevWaterScore = lerpValue(waterScore, prevWaterScore, 10);
        dispString = valToString(prevWaterScore, 3);
        waterScoreDisplay.innerHTML = dispString;
        waterScorePDisplay.innerHTML = valToString(Math.floor(prevWaterScore/totalScore*100))+"% of total";
        var diff = percentDifference(lastWaterScore, prevWaterScore)*-1;
        if(diff > 0){
            waterProgress.innerHTML = "better than previous";
            waterProgressVal.style.color = "rgb(68, 213, 13)";
        }else if(diff==0){
            waterProgress.innerHTML = "same as previous";
            waterProgressVal.style.color = 'white';
        }else{
            waterProgress.innerHTML = "worse than previous";
            waterProgressVal.style.color = "rgb(217, 53, 53)";
        }
        waterProgressVal.innerHTML = valToString(diff,2)+"%";
    };
    if(prevPowerScore != powerScore){
        prevPowerScore = lerpValue(powerScore, prevPowerScore, 10);
        dispString = valToString(prevPowerScore, 3);
        powerScoreDisplay.innerHTML = dispString;
        powerScorePDisplay.innerHTML = valToString(Math.floor(prevPowerScore/totalScore*100))+"% of total";
        var diff = percentDifference(lastPowerScore, prevPowerScore)*-1;
        if(diff > 0){
            powerProgress.innerHTML = "better than previous";
            powerProgressVal.style.color = "rgb(68, 213, 13)";
        }else if(diff==0){
            powerProgress.innerHTML = "same as previous";
            powerProgressVal.style.color = 'white';
        }else{
            powerProgress.innerHTML = "worse than previous";
            powerProgressVal.style.color = "rgb(217, 53, 53)";
        }
        powerProgressVal.innerHTML = valToString(diff,2)+"%";
    };

    // lower half page info
    var waterCostDiff = lastWaterScore*cost24Water - prevWaterScore*cost24Water;
    var powerCostDiff = lastPowerScore*cost24Water - lastPowerScore*cost24Water;
    var totalCostDiff = waterCostDiff + powerCostDiff;
    totalCostDiff = totalCostDiff.toFixed(2);
    lowerInfo.innerHTML = "$"+totalCostDiff.toString()+"/HR";
}