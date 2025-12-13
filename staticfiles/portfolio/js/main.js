function scrollSkills(direction) {
    const carousel = document.getElementById('skillsCarousel');
    if (carousel) {
        const scrollAmount = 200;
        carousel.scrollBy({
            left: direction * scrollAmount,
            behavior: 'smooth'
        });
    }
}

let touchStartX = 0;
let touchEndX = 0;

document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.querySelector('.navbar');
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const html = document.documentElement;
    
    const savedTheme = localStorage.getItem('theme') || 'dark';
    html.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);
    
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = html.getAttribute('data-theme');
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            html.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
        });
    }
    
    function updateThemeIcon(theme) {
        if (themeIcon) {
            if (theme === 'dark') {
                themeIcon.classList.remove('fa-sun');
                themeIcon.classList.add('fa-moon');
            } else {
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
            }
        }
    }

    const skillsCarousel = document.getElementById('skillsCarousel');
    if (skillsCarousel) {
        skillsCarousel.addEventListener('touchstart', function(e) {
            touchStartX = e.changedTouches[0].screenX;
        }, false);
        
        skillsCarousel.addEventListener('touchend', function(e) {
            touchEndX = e.changedTouches[0].screenX;
            handleSkillsSwipe();
        }, false);
    }
    
    function handleSkillsSwipe() {
        const swipeThreshold = 50;
        if (touchStartX - touchEndX > swipeThreshold) {
            scrollSkills(1);
        }
        if (touchEndX - touchStartX > swipeThreshold) {
            scrollSkills(-1);
        }
    }

    initProjectCarousels();

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.project-card, .skill-card, .course-card, .certificate-card').forEach(el => {
        el.classList.add('animate-ready');
        observer.observe(el);
    });

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateY(-10px)';
            setTimeout(() => alert.remove(), 300);
        }, 5000);
    });
});

function initProjectCarousels() {
    const carousels = document.querySelectorAll('[data-carousel]');
    
    carousels.forEach(carousel => {
        const slides = carousel.querySelectorAll('.carousel-slide');
        const dots = carousel.querySelectorAll('.dot');
        const prevBtn = carousel.querySelector('.carousel-nav.prev');
        const nextBtn = carousel.querySelector('.carousel-nav.next');
        
        if (slides.length <= 1) return;
        
        let currentIndex = 0;
        let startX = 0;
        let endX = 0;
        let isDragging = false;
        
        function showSlide(index) {
            if (index >= slides.length) index = 0;
            if (index < 0) index = slides.length - 1;
            
            slides.forEach((slide, i) => {
                slide.classList.toggle('active', i === index);
            });
            
            dots.forEach((dot, i) => {
                dot.classList.toggle('active', i === index);
            });
            
            currentIndex = index;
        }
        
        if (prevBtn) {
            prevBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                showSlide(currentIndex - 1);
            });
        }
        
        if (nextBtn) {
            nextBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                showSlide(currentIndex + 1);
            });
        }
        
        dots.forEach((dot, i) => {
            dot.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                showSlide(i);
            });
        });
        
        carousel.addEventListener('touchstart', (e) => {
            startX = e.touches[0].clientX;
            isDragging = true;
        }, { passive: true });
        
        carousel.addEventListener('touchmove', (e) => {
            if (!isDragging) return;
            endX = e.touches[0].clientX;
        }, { passive: true });
        
        carousel.addEventListener('touchend', () => {
            if (!isDragging) return;
            isDragging = false;
            
            const diff = startX - endX;
            const threshold = 50;
            
            if (Math.abs(diff) > threshold) {
                if (diff > 0) {
                    showSlide(currentIndex + 1);
                } else {
                    showSlide(currentIndex - 1);
                }
            }
            
            startX = 0;
            endX = 0;
        });
        
        carousel.addEventListener('mousedown', (e) => {
            startX = e.clientX;
            isDragging = true;
            carousel.style.cursor = 'grabbing';
        });
        
        carousel.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            endX = e.clientX;
        });
        
        carousel.addEventListener('mouseup', () => {
            if (!isDragging) return;
            isDragging = false;
            carousel.style.cursor = 'grab';
            
            const diff = startX - endX;
            const threshold = 50;
            
            if (Math.abs(diff) > threshold) {
                if (diff > 0) {
                    showSlide(currentIndex + 1);
                } else {
                    showSlide(currentIndex - 1);
                }
            }
            
            startX = 0;
            endX = 0;
        });
        
        carousel.addEventListener('mouseleave', () => {
            isDragging = false;
            carousel.style.cursor = 'grab';
        });
    });
}
