$(document).ready(function () {
    $('#menu').click(function () {
        $(this).toggleClass('fa-times');
        $('.navbar').toggleClass('nav-toggle');
    });
    $(window).on('scroll load', function () {
        $('#menu').removeClass('fa-times');
        $('.navbar').removeClass('nav-toggle');

        if (window.scrollY > 60) {
            document.querySelector('#scroll-top').classList.add('active');
        } else {
            document.querySelector('#scroll-top').classList.remove('active');
        }

        // scroll spy
        $('section').each(function () {
            let height = $(this).height();
            let offset = $(this).offset().top - 200;
            let top = $(window).scrollTop();
            let id = $(this).attr('id');

            if (top > offset && top < offset + height) {
                $('.navbar ul li a').removeClass('active');
                $('.navbar').find(`[href="#${id}"]`).addClass('active');
            }
        });
    });

    // smooth scrolling
    $('a[href*="#"]').on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top,
        }, 500, 'linear')
    });

});
 // <!-- emailjs to mail contact form data -->
 $("#contact-form").submit(function (event) {
    emailjs.init("user_TTDmetQLYgWCLzHTDgqxm");

    emailjs.sendForm('contact_service', 'template_contact', '#contact-form')
        .then(function (response) {
            console.log('SUCCESS!', response.status, response.text);
            document.getElementById("contact-form").reset();
        }, function (error) {
            console.log('FAILED...', error);
        });
    event.preventDefault();
});
// <!-- emailjs to mail contact form data -->



// <!-- tilt js effect starts -->
VanillaTilt.init(document.querySelectorAll(".tilt"), {
    max: 15,
});
// <!-- tilt js effect ends -->


// pre loader start
function loader() {
    document.querySelector('.loader-container').classList.add('fade-out');
}
function fadeOut() {
    setInterval(loader, 500);
}
window.onload = fadeOut;
// pre loader end

// // disable developer mode
// document.onkeydown = function (e) {
//     if (e.keyCode == 123) {
//         return true;
//     }
//     if (e.ctrlKey && e.shiftKey && e.keyCode == 'I'.charCodeAt(0)) {
//         return true;
//     }
//     if (e.ctrlKey && e.shiftKey && e.keyCode == 'C'.charCodeAt(0)) {
//         return true;
//     }
//     if (e.ctrlKey && e.shiftKey && e.keyCode == 'J'.charCodeAt(0)) {
//         return true;
//     }
//     if (e.ctrlKey && e.keyCode == 'U'.charCodeAt(0)) {
//         return true;
//     }
// }

// Start of Tawk.to Live Chat
var Tawk_API = Tawk_API || {}, Tawk_LoadStart = new Date();
(function () {
    var s1 = document.createElement("script"), s0 = document.getElementsByTagName("script")[0];
    s1.async = true;
    s1.src = 'https://embed.tawk.to/60df10bf7f4b000ac03ab6a8/1f9jlirg6';
    s1.charset = 'UTF-8';
    s1.setAttribute('crossorigin', '*');
    s0.parentNode.insertBefore(s1, s0);
})();
// End of Tawk.to Live Chat


/* ===== SCROLL REVEAL ANIMATION ===== */
const srtop = ScrollReveal({
    origin: 'top',
    distance: '80px',
    duration: 1000,
    reset: true
});

/* SCROLL HOME */
srtop.reveal('.home .content h3', { delay: 200 });
srtop.reveal('.home .content p', { delay: 200 });
srtop.reveal('.home .content .btn', { delay: 200 });

srtop.reveal('.home .image', { delay: 400 });
srtop.reveal('.home .linkedin', { interval: 600 });
srtop.reveal('.home .github', { interval: 800 });
srtop.reveal('.home .twitter', { interval: 1000 });
srtop.reveal('.home .telegram', { interval: 600 });
srtop.reveal('.home .instagram', { interval: 600 });
srtop.reveal('.home .dev', { interval: 600 });

/* SCROLL ABOUT */
srtop.reveal('.about .content h3', { delay: 200 });
srtop.reveal('.about .content .tag', { delay: 200 });
srtop.reveal('.about .content p', { delay: 200 });
srtop.reveal('.about .content .box-container', { delay: 200 });
srtop.reveal('.about .content .resumebtn', { delay: 200 });






/* SCROLL EXPERIENCE */
srtop.reveal('#background .timeline', { delay: 400 });
srtop.reveal('#background .timeline .container', { interval: 400 });

/* SCROLL CONTACT */
srtop.reveal('.contact .container', { delay: 400 });
srtop.reveal('.contact .container .form-group', { delay: 400 });





