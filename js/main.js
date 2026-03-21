// Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.offsetTop - headerHeight;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
                
                // Close mobile menu if open
                document.querySelector('.nav')?.classList.remove('active');
            }
        });
    });
    
    // Mobile menu toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const nav = document.querySelector('.nav');
    
    if (mobileMenuBtn && nav) {
        mobileMenuBtn.addEventListener('click', function() {
            nav.classList.toggle('active');
            const icon = this.querySelector('i');
            if (nav.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!nav.contains(e.target) && !mobileMenuBtn.contains(e.target)) {
                nav.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }
    
    // Header scroll effect
    const header = document.querySelector('.header');
    const scrollTop = document.getElementById('scrollTop');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        // Header shadow
        if (currentScroll > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
        
        // Scroll to top button
        if (currentScroll > 500) {
            scrollTop.classList.add('visible');
        } else {
            scrollTop.classList.remove('visible');
        }
        
        lastScroll = currentScroll;
    });
    
    // Scroll to top functionality
    if (scrollTop) {
        scrollTop.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }
    
    // Active navigation link on scroll
    const sections = document.querySelectorAll('section[id]');
    
    window.addEventListener('scroll', function() {
        const scrollY = window.pageYOffset;
        const headerHeight = header.offsetHeight;
        
        sections.forEach(section => {
            const sectionHeight = section.offsetHeight;
            const sectionTop = section.offsetTop - headerHeight - 100;
            const sectionId = section.getAttribute('id');
            
            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                document.querySelectorAll('.nav a').forEach(link => {
                    link.classList.remove('active');
                });
                const activeLink = document.querySelector('.nav a[href="#' + sectionId + '"]');
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    });
    
    // Form submission
    const contactForm = document.querySelector('.contact-form form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const data = {};
            formData.forEach((value, key) => {
                data[key] = value;
            });
            
            // Show loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;
            submitBtn.textContent = '发送中...';
            submitBtn.disabled = true;
            
            // Simulate sending (replace with actual API call)
            setTimeout(() => {
                alert('感谢您的询价！我们会尽快与您联系。\n\nThank you for your inquiry! We will contact you soon.');
                this.reset();
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }, 1000);
        });
    }
    
    // Intersection Observer for scroll animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Elements to animate
    const animateElements = document.querySelectorAll('.product-card, .advantage-item, .stat-item, .factory-item, .contact-item');
    
    animateElements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.animationDelay = `${index * 0.1}s`;
        observer.observe(element);
    });
    
    // Counter animation for stats
    const animateCounter = (element, target, hasPlus) => {
        let current = 0;
        const increment = target / 50;
        const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
                element.innerHTML = target + (hasPlus ? '<span style="font-size:28px">+</span>' : '');
                clearInterval(timer);
            } else {
                element.innerHTML = Math.floor(current) + (hasPlus ? '<span style="font-size:28px">+</span>' : '');
            }
        }, 30);
    };
    
    // Observe hero stats for counter animation
    const heroStats = document.querySelectorAll('.hero-stat-number');
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const text = entry.target.textContent;
                const number = parseInt(text);
                if (!isNaN(number)) {
                    const hasPlus = text.includes('+');
                    entry.target.innerHTML = '0' + (hasPlus ? '<span style="font-size:28px">+</span>' : '');
                    setTimeout(() => {
                        animateCounter(entry.target, number, hasPlus);
                    }, 300);
                }
                statsObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });
    
    heroStats.forEach(stat => statsObserver.observe(stat));
    
    // Parallax effect for hero section
    const hero = document.querySelector('.hero');
    if (hero) {
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            if (scrolled < window.innerHeight) {
                hero.style.backgroundPositionY = `${scrolled * 0.5}px`;
            }
        });
    }
    
    // Product card hover effect
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // Add loading animation
    window.addEventListener('load', function() {
        document.body.classList.add('loaded');
    });
    
});

// Add CSS for nav active state on mobile (dark theme)
const style = document.createElement('style');
style.textContent = `
    @media (max-width: 768px) {
        .nav.active {
            display: flex !important;
            position: fixed;
            top: 70px;
            left: 0;
            right: 0;
            background: rgba(10, 14, 23, 0.98);
            backdrop-filter: blur(20px);
            flex-direction: column;
            padding: 24px;
            border-bottom: 1px solid rgba(255, 107, 44, 0.2);
            z-index: 999;
        }
        
        .nav.active ul {
            flex-direction: column;
            gap: 0;
        }
        
        .nav.active li {
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        
        .nav.active a {
            display: block;
            padding: 16px 0;
            color: #a0aec0;
        }
        
        .nav.active a:hover,
        .nav.active a.active {
            color: #ff6b2c;
        }
        
        .nav.active .lang-switch {
            margin-top: 20px;
            margin-left: 0;
            justify-content: center;
        }
    }
    
    /* Animation for elements appearing */
    .animate-in {
        animation: fadeInUp 0.6s ease-out forwards !important;
    }
    
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Typing cursor effect */
    .typing-cursor {
        display: inline-block;
        width: 3px;
        height: 1em;
        background: #ff6b2c;
        margin-left: 4px;
        animation: blink 1s infinite;
    }
    
    @keyframes blink {
        0%, 50% { opacity: 1; }
        51%, 100% { opacity: 0; }
    }
`;
document.head.appendChild(style);
