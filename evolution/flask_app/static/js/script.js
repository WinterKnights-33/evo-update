

function next(){
    document.getElementById('log').style.display = "none";
    document.getElementById('regis').style.display = "block";
    }
    function prev(){
    document.getElementById('regis').style.display = "none";
    document.getElementById('log').style.display = "block";
    }



const pass_field = document.querySelector(".pass-key");
const showBtn = document.querySelector(".show");

showBtn.addEventListener("click", function() {
    if(pass_field.type === "password") {
        pass_field.type = "text";
        showBtn.textContent = "HIDE";
        showBtn.style.color = "#3498db";
    } else {
        pass_field.type = "password";
        showBtn.textContent = "SHOW";
        showBtn.style.color = "#222";
    }
});

var introDiv = document.querySelector(".intro");

function accept() {
    introDiv.remove();
}

function fruits() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.fontStyle == "oblique") {
        e.style.fontStyle = "normal"
    }
    else {
        e.style.fontStyle = "oblique"
    }
    return true;
}

function veggies() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.wordSpacing == "1px") {
        e.style.wordSpacing = "normal"
    }
    else {
        e.style.wordSpacing = "1px"
    }
    return true;
}

function dairyFree() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.wordSpacing == "-1px") {
        e.style.wordSpacing = "normal"
    }
    else {
        e.style.wordSpacing = "-1px"
    }
    return true;
}

function fish() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.lineHeight == "120%") {
        e.style.lineHeight = "100%"
    }
    else {
        e.style.lineHeight = "120%"
    }
    return true;
}

function hardFoods() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.fontSize == "large") {
        e.style.fontSize = "small"
    }
    else {
        e.style.fontSize = "large"
    }
    return true;
}

function nuts() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.fontSize == "150%") {
        e.style.fontSize = "100%"
    }
    else {
        e.style.fontSize = "150%"
    }
    return true;
}

function meat() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.fontWeight == "900") {
        e.style.fontWeight = "100"
    }
    else {
        e.style.fontWeight = "900"
    }
    return true;
}

function update() {
    var e = document.getElementById("sk");

    if (!e) return true;
    if (e.style.fontWeight == "normal") {
        e.style.fontWeight = "100"
    }
    else {
        e.style.fontWeight = "normal"
    }
    return true;
}

registerProperty({
    name: "--p",
    syntax: "<integer>",
    initialValue: 0,
    inherits: true,
    });