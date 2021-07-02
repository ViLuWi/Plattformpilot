// create cookie
let cookie_set = false


function countCookieLawNumber(all) {
    let cookie_number = ''
    if (document.getElementById('necessary').checked || all == 'all') {
        cookie_number += 'necessary ';
    }
    if (document.getElementById('tracking').checked || all == 'all') {
        cookie_number += 'tracking ';
    }
    if (document.getElementById('marketing').checked || all == 'all') {
        cookie_number += 'marketing ';
    }
    checkCookie()
    if (!cookie_set) {
        setCookie('law_cookie', cookie_number, 90)
    } else {
        setCookie('law_cookie', cookie_number, 90)
    }
    window.location.reload()    // reload to see changes
}

function setCookie(name, value, daysToLive) {
    // Encode value in order to escape semicolons, commas, and whitespace
    let cookie = name + "=" + encodeURIComponent(value);

    if (typeof daysToLive === "number") {
        /* Sets the max-age attribute so that the cookie expires
        after the specified number of days */
        cookie += ";max-age=" + (daysToLive * 24 * 60 * 60) + ';Secure;path=/';

        document.cookie = cookie;
        cookie_set = true

    }
}

function getCookie(name) {
    // Split cookie string and get all individual name=value pairs in an array
    let cookieArr = document.cookie.split(";");

    // Loop through the array elements
    for (let i = 0; i < cookieArr.length; i++) {
        let cookiePair = cookieArr[i].split("=");

        /* Removing whitespace at the beginning of the cookie name
        and compare it with the given string */
        if (name == cookiePair[0].trim()) {
            // Decode the cookie value and return
            return decodeURIComponent(cookiePair[1]);
        }
    }
    return null;
}

function renewCookie() {
    countCookieLawNumber('custom')
}

// check if cookie exist
function checkCookie() {
    // Get cookie using getCookie function
    let cookie = getCookie("law_cookie");
    if (cookie !== "" && cookie !== null) {
        cookie_set = true
    } else {
        cookie_set = false
    }
}

checkCookie()

// do stuff if related to cookie selection
let doStuff = () => {
    if (cookie_set) {
        if (document.cookie.includes('tracking')) {
            console.log('tracking on')
        }
        if (document.cookie.includes('google')) {
            console.log('google on')
        }
        if (document.cookie.includes('marketing')) {
            console.log('marketing on')
        }
    } else {
        document.getElementById('cookie__wrapper').classList.remove('d-none')
    }
}
window.addEventListener('load', doStuff)