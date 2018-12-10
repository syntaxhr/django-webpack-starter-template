import Swiper from 'swiper'
import 'swiper/dist/css/swiper.min.css'


window.render_slider = function (props) {

    // Docs: https://idangero.us/swiper/api/#parameters
    if (props.name) {

        let config = {
            // Optional parameters
            direction: 'horizontal',
            loop: true,
            speed: 400,
            slidesPerView: 1,
            spaceBetween: 0,
            effect: 'fade',
            // breakpoints: {
            //     // when window width is >= 480px
            //     640: {
            //         slidesPerView: 1
            //     },
            //     // when window width is >= 960px
            //     960: {
            //         slidesPerView: 3
            //     },
            //     // when window width is >= 1280px
            //     // 1280: {
            //     //     slidesPerView: 5,
            //     //     spaceBetween: 0
            //     // },
            // },

            // Navigation arrows
            navigation: {
                nextEl: props.name + 'next',
                prevEl: props.name + 'prev',
            },

        }

        // Docs: https://idangero.us/swiper/api/#parameters
        new Swiper(props.name, Object.assign(config, props))

    }
}


