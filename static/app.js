// SIDEBAR

const btn = document.querySelector(".btn");
const feat_btn = document.querySelector(".feat-btn");
const feat_show = document.querySelector(".feat-show");
const first = document.querySelector(".first");
const sidebar = document.querySelector(".sidebar");
const links = document.querySelectorAll("nav ul li a");

btn.addEventListener("click", () => {
  btn.classList.toggle("click");
  sidebar.classList.toggle("show");
});
feat_btn.addEventListener("click", () => {
  feat_show.classList.toggle("show");
  first.classList.toggle("rotate");
});

for (var i = 0, length = links.length; i < length; i++) {
  links[i].onclick = function () {
    let linkItem = document.querySelector("nav li.active");
    if (linkItem) linkItem.classList.remove("active");
    this.parentNode.classList.add("active");
  };
}

// LOGIN FORM
const signinBtn = document.querySelector(".signinBtn");
const signupBtn = document.querySelector(".signupBtn");
const formBx = document.querySelector(".formBx");

signupBtn.onclick = function () {
  formBx.classList.add("active");
};

signinBtn.onclick = function () {
  formBx.classList.remove("active");
};
