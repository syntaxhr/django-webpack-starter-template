let submenuToggle = document.querySelector('.submenu-toggle');

if (submenuToggle) {
    document.querySelectorAll('.submenu-toggle').forEach(button => {
        button.addEventListener('click', event => {
            event.stopPropagation()

            // Open or close dropdown menu
            const li = button.parentNode
            if (li.classList.contains('show')) {
                li.classList.remove('show')
            }
            else {
                li.classList.add('show')
            }

            // Rotate chevron icon
            if (button.classList.contains('rotated')) {
                button.classList.remove('rotated')
            }
            else {
                button.classList.add('rotated')
            }
        })
    })
}


let mobileMenuToggle = document.querySelector('.mobile-menu-toggle');

if (mobileMenuToggle) {
    document.querySelector('.mobile-menu-toggle').addEventListener('click', () => {

        const navTop = document.querySelector('.main-nav__top__right')
        const navBottom = document.querySelector('.main-nav__bottom')

        // Show/Hide top navigation
        if (navTop.classList.contains('show')) {
            navTop.classList.remove('show')
            navTop.querySelectorAll('li').forEach(li => {
                if (li.classList.contains('show')) {
                    li.classList.remove('show')
                }
            })
        }
        else {
            navTop.classList.add('show')
        }

        // Show/hide bottom navigation
        if (navBottom.classList.contains('show')) {
            navBottom.classList.remove('show')
            navBottom.querySelectorAll('li').forEach(li => {
                if (li.classList.contains('show')) {
                    li.classList.remove('show')
                }
            })
        }
        else {
            navBottom.classList.add('show')
        }
    })
}
