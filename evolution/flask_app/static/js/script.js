

const pass_register = document.querySelector(".pass_reg");
const showLogin = document.querySelector(".showLog");

showLogin.addEventListener("click", function() {
    if(pass_register.type === "register") {
        pass_register.type = "text";
        showLogin.textContent = "HIDE";
    } else {
        pass_register.type = "login";
        showLogin.textContent = "SHOW";
    }
});




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