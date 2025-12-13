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

    const themeToggleDesktop = document.getElementById('themeToggleDesktop');
    const themeToggleFloat = document.getElementById('themeToggleFloat');
    const themeIconDesktop = document.getElementById('themeIconDesktop');
    const themeIconFloat = document.getElementById('themeIconFloat');
    const html = document.documentElement;
    
    const savedTheme = localStorage.getItem('theme') || 'dark';
    html.setAttribute('data-theme', savedTheme);
    updateThemeIcons(savedTheme);
    
    function toggleTheme() {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);
        updateThemeIcons(newTheme);
    }
    
    if (themeToggleDesktop) {
        themeToggleDesktop.addEventListener('click', toggleTheme);
    }
    
    if (themeToggleFloat) {
        themeToggleFloat.addEventListener('click', toggleTheme);
    }
    
    function updateThemeIcons(theme) {
        const icons = [themeIconDesktop, themeIconFloat];
        icons.forEach(icon => {
            if (icon) {
                if (theme === 'dark') {
                    icon.classList.remove('fa-sun');
                    icon.classList.add('fa-moon');
                } else {
                    icon.classList.remove('fa-moon');
                    icon.classList.add('fa-sun');
                }
            }
        });
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
    initProjectModal();

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

function initProjectModal() {
    const modal = document.getElementById('projectModal');
    if (!modal) return;
    
    const backdrop = modal.querySelector('.project-modal-backdrop');
    const closeBtn = modal.querySelector('.project-modal-close');
    const carouselInner = document.getElementById('modalCarouselInner');
    const carouselDots = document.getElementById('modalCarouselDots');
    const titleEl = document.getElementById('modalProjectTitle');
    const descEl = document.getElementById('modalProjectDescription');
    const skillsEl = document.getElementById('modalProjectSkills');
    const linksEl = document.getElementById('modalProjectLinks');
    const prevBtn = modal.querySelector('.carousel-nav.prev');
    const nextBtn = modal.querySelector('.carousel-nav.next');
    
    let currentIndex = 0;
    let slides = [];
    let dots = [];

    document.querySelectorAll('.project-card').forEach(card => {
        card.style.cursor = 'pointer';
        
        card.addEventListener('click', (e) => {
            if (e.target.closest('a') || e.target.closest('button')) return;
            
            const title = card.dataset.projectTitle || '';
            const desc = card.dataset.projectDescription || '';
            
            let images = [];
            try {
                images = JSON.parse(card.dataset.projectImages || '[]');
            } catch (err) {
                images = [];
            }
            
            let skillTags = [];
            try {
                const skillsData = JSON.parse(card.dataset.projectSkills || '[]');
                skillTags = skillsData.map(s => ({
                    name: s.name,
                    imgSrc: s.img || null
                }));
            } catch (err) {
                skillTags = [];
            }
            
            const links = [];
            const repoUrl = card.dataset.projectRepo;
            const demoUrl = card.dataset.projectDemo;
            
            if (repoUrl) {
                links.push({
                    href: repoUrl,
                    text: 'GitHub',
                    classes: 'btn btn-sm btn-outline-primary',
                    icon: 'fab fa-github'
                });
            }
            if (demoUrl) {
                links.push({
                    href: demoUrl,
                    text: 'Demo',
                    classes: 'btn btn-sm btn-primary',
                    icon: 'fas fa-external-link-alt'
                });
            }
            
            openModal(title, desc, images, skillTags, links);
        });
    });
    
    function openModal(title, description, images, skills, links) {
        titleEl.textContent = title;
        descEl.textContent = description;
        
        carouselInner.innerHTML = '';
        carouselDots.innerHTML = '';
        
        if (images.length > 0 && images[0] !== '') {
            images.forEach((src, i) => {
                const slide = document.createElement('div');
                slide.className = 'carousel-slide' + (i === 0 ? ' active' : '');
                slide.innerHTML = `<img src="${src}" alt="${title} - Imagem ${i + 1}">`;
                carouselInner.appendChild(slide);
                
                if (images.length > 1) {
                    const dot = document.createElement('span');
                    dot.className = 'dot' + (i === 0 ? ' active' : '');
                    dot.dataset.index = i;
                    carouselDots.appendChild(dot);
                }
            });
        } else {
            const slide = document.createElement('div');
            slide.className = 'carousel-slide active';
            slide.innerHTML = `<div style="display:flex;align-items:center;justify-content:center;height:100%;"><i class="fas fa-folder-open" style="font-size:80px;color:var(--text-muted);"></i></div>`;
            carouselInner.appendChild(slide);
        }
        
        slides = modal.querySelectorAll('.carousel-slide');
        dots = modal.querySelectorAll('.carousel-dots .dot');
        currentIndex = 0;
        
        skillsEl.innerHTML = '';
        skills.forEach(skill => {
            const tag = document.createElement('span');
            tag.className = 'project-skill-tag';
            tag.innerHTML = skill.imgSrc ? `<img src="${skill.imgSrc}" alt="${skill.name}">` : '';
            tag.innerHTML += skill.name;
            skillsEl.appendChild(tag);
        });
        
        linksEl.innerHTML = '';
        links.forEach(link => {
            const a = document.createElement('a');
            a.href = link.href;
            a.className = link.classes;
            a.target = '_blank';
            if (link.icon) {
                a.innerHTML = `<i class="${link.icon}"></i> ${link.text}`;
            } else {
                a.textContent = link.text;
            }
            linksEl.appendChild(a);
        });
        
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
        
        initModalCarousel();
    }
    
    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }
    
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
    
    function initModalCarousel() {
        dots = modal.querySelectorAll('.carousel-dots .dot');
        dots.forEach((dot, i) => {
            dot.addEventListener('click', () => showSlide(i));
        });
    }
    
    if (prevBtn) {
        prevBtn.addEventListener('click', () => showSlide(currentIndex - 1));
    }
    
    if (nextBtn) {
        nextBtn.addEventListener('click', () => showSlide(currentIndex + 1));
    }
    
    if (backdrop) {
        backdrop.addEventListener('click', closeModal);
    }
    
    if (closeBtn) {
        closeBtn.addEventListener('click', closeModal);
    }
    
    document.addEventListener('keydown', (e) => {
        if (!modal.classList.contains('active')) return;
        
        if (e.key === 'Escape') {
            closeModal();
        } else if (e.key === 'ArrowLeft') {
            showSlide(currentIndex - 1);
        } else if (e.key === 'ArrowRight') {
            showSlide(currentIndex + 1);
        }
    });
    
    let touchStartX = 0;
    let touchEndX = 0;
    
    const modalCarousel = modal.querySelector('.project-modal-carousel');
    if (modalCarousel) {
        modalCarousel.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
        }, { passive: true });
        
        modalCarousel.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].clientX;
            const diff = touchStartX - touchEndX;
            if (Math.abs(diff) > 50) {
                if (diff > 0) {
                    showSlide(currentIndex + 1);
                } else {
                    showSlide(currentIndex - 1);
                }
            }
        });
    }
}
