// scrollspy subnav
const links = document.querySelectorAll(".scrollspy-link");
const sections = document.querySelectorAll(".scrollspy-section");
const indicator = document.querySelector(".scrollspy-indicator");
links.forEach((link) => {
    link.onclick = () => {
        sections.forEach((section) => {
            if (link.dataset.target === section.id) {
                document.documentElement.scrollTop = section.offsetTop;
            }
        });
    };
});
window.onscroll = () => scrollspy();
window.onresize = () => scrollspy();
const scrollspy = () => {
    const pageYPosition = document.documentElement.scrollTop || document.body.scrollTop;
    sections.forEach((section) => {
        const sectionYPosition = section.offsetTop;
        if (pageYPosition > sectionYPosition - 60) {
            links.forEach((link) => {
                if (link.dataset.target === section.id) {
                    indicator.style.left = `${link.offsetLeft}px`;
                    indicator.style.width = `${link.offsetWidth}px`;
                }
            });
        }
    });
};
scrollspy();

// fix position when scroll
window.addEventListener('scroll', () => {
    const scroll_nav = document.getElementsByClassName('scrollspy-nav')[0]
    if (window.scrollY > 430 && window.innerWidth > 575) {
        scroll_nav.classList.add('fix-scrollspy')
    } else if (window.scrollY > 545 && window.innerWidth <= 575) {
        scroll_nav.classList.add('fix-scrollspy')
    } else if (window.scrollY < 430 && window.innerWidth > 575) {
        scroll_nav.classList.remove('fix-scrollspy')
    } else if (window.scrollY < 545 && window.innerWidth <= 575) {
        scroll_nav.classList.remove('fix-scrollspy')
    }
})