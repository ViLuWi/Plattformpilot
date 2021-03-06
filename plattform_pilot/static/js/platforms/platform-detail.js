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
        if (pageYPosition > sectionYPosition - 100) {
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

// check submitted rating form
const rating = document.querySelectorAll('input[name="rating"]')
const author_input = document.getElementById('id_author')
let check_rating = () => {
    for (let i = 1; i <= rating.length; i++) {
        if (document.getElementById('radio'+i).checked) {
            if (author_input.value !== '') {
                document.getElementById('form').submit();
            } else {
                author_input.style.border = '2px solid var(--danger)'
            }
        } else {
            console.log('Kein rating')
        }
    }
}


// Animate on scroll
AOS.init({
    once: true
})