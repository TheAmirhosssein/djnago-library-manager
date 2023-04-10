const menuButton = document.querySelector(".menu");
const textsOfMenu = document.querySelectorAll(".text-menu");
const navigation = document.querySelector(".navigation");
const boxTwo = document.querySelector(".box-two");
const boxThree = document.querySelector(".box-three");

const logo = document.querySelector(".logo");
const textMenu = document.querySelectorAll(".text-for-menu");
const a = document.querySelectorAll("li a.tag-a");


const form = document.querySelector("form");
const formLogo = document.querySelector("form .logo");
const inputs = document.querySelector(".inputs")
{
    form.classList.add("open");
    setTimeout(() => {
        formLogo.classList.add("to-show");
        inputs.classList.add("to-show");
    }, 2000)
}

let device;
if(/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) device = 'm';
else device='p';

if(device === 'm'){
    navigation.classList.toggle("animation-menu");
    navigation.classList.toggle("animation-menu-deactive");
    logo.classList.toggle("logo-container-active");
    logo.querySelector(".logo-image").classList.toggle("logo-active")
    logo.querySelector(".logo-text").classList.toggle("hide");
    logo.querySelector(".logo-text").classList.toggle("show");
    logo.querySelector(".logo-image").classList.toggle("logo-deactive")
    logo.classList.toggle("logo-container-deactive");
    setTimeout(() => {
        boxTwo.classList.toggle("hide");
        boxThree.classList.toggle("hide");
        boxTwo.classList.toggle("show");
        boxThree.classList.toggle("show");

        textMenu.forEach((item) => {
            item.classList.toggle("show");
            item.classList.toggle("hide");
        })
    }, 800);

    
    // textMenu.classList.toggle("text-menu");
    // textMenu.classList.toggle("text-menu-deactive");
    a.forEach(item => {
        item.classList.toggle("close");
    })
}

menuButton.addEventListener("click", () => {
    navigation.classList.toggle("animation-menu");
    navigation.classList.toggle("animation-menu-deactive");
    logo.classList.toggle("logo-container-active");
    logo.querySelector(".logo-image").classList.toggle("logo-active")
    logo.querySelector(".logo-text").classList.toggle("hide");
    logo.querySelector(".logo-text").classList.toggle("show");
    logo.querySelector(".logo-image").classList.toggle("logo-deactive")
    logo.classList.toggle("logo-container-deactive");
    setTimeout(() => {
        boxTwo.classList.toggle("hide");
        boxThree.classList.toggle("hide");
        boxTwo.classList.toggle("show");
        boxThree.classList.toggle("show");

        textMenu.forEach((item) => {
            item.classList.toggle("show");
            item.classList.toggle("hide");
        })
    }, 800);

    
    // textMenu.classList.toggle("text-menu");
    // textMenu.classList.toggle("text-menu-deactive");
    a.forEach(item => {
        item.classList.toggle("close");
    })
});
