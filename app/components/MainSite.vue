<script setup>
import { onMounted, ref } from 'vue'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import Lenis from 'lenis'
import CustomCursor from './CustomCursor.vue'
import ModernHero from './ModernHero.vue'
import OffersCarousel from './OffersCarousel.vue'
import PremiumMenu from './PremiumMenu.vue'
import HeritageStory from './HeritageStory.vue'
import AboutSection from './AboutSection.vue'
import ReviewsMarquee from './ReviewsMarquee.vue'
import FilmGrain from './FilmGrain.vue'

onMounted(() => {
  // Initialize Lenis for smooth momentum scrolling
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    direction: 'vertical',
    gestureDirection: 'vertical',
    smooth: true,
  })
  
  function raf(time) {
    lenis.raf(time)
    requestAnimationFrame(raf)
  }
  requestAnimationFrame(raf)

  // Tie GSAP to Lenis
  lenis.on('scroll', ScrollTrigger.update)
  gsap.ticker.add((time) => {
    lenis.raf(time * 1000)
  })
  gsap.ticker.lagSmoothing(0)

  // Premium Cinematic Reveal Engine
  gsap.registerPlugin(ScrollTrigger)
  const sections = document.querySelectorAll('.perspective-section')
  
  sections.forEach((sec) => {
    // Elegant entrance: Blur un-filter, scale down slightly from zoom, fade in, move up
    gsap.fromTo(sec, 
      {
        y: 80,
        opacity: 0,
        scale: 1.03,
        filter: 'blur(15px)'
      },
      {
        scrollTrigger: {
          trigger: sec,
          start: 'top 85%',
          toggleActions: 'play none none reverse'
        },
        y: 0,
        opacity: 1,
        scale: 1,
        filter: 'blur(0px)',
        duration: 1.5,
        ease: 'power3.out'
      }
    )
  })

  // Global Magnetic Buttons
  const magneticBtns = document.querySelectorAll('.magnetic-btn')
  magneticBtns.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect()
      const x = (e.clientX - rect.left - rect.width / 2) * 0.3
      const y = (e.clientY - rect.top - rect.height / 2) * 0.3
      gsap.to(btn, { x, y, duration: 0.5, ease: 'power2.out' })
    })
    btn.addEventListener('mouseleave', () => {
      gsap.to(btn, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.3)' })
    })
  })
})
</script>

<template>
  <div class="site-wrapper">
    <CustomCursor />
    <FilmGrain />
    
    <nav class="navbar glass-panel">
      <div class="logo">
        <!-- User Uploaded Logo (Background Removed) -->
        <img src="/images/logo.png" alt="Malabar Chef Logo" class="nav-logo-img" />
      </div>
      <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#offers">Offers</a></li>
        <li><a href="#menu">Menu</a></li>
        <li><a href="#about">About</a></li>
      </ul>
    </nav>

    <header id="home" class="perspective-section" style="position:relative; z-index: 5;">
      <ModernHero />
    </header>

    <!-- 3D Offers Carousel -->
    <section id="offers" class="perspective-section" style="position:relative; z-index: 4;">
      <OffersCarousel />
    </section>

    <!-- Visual Menu Section -->
    <section id="menu" class="perspective-section" style="position:relative; z-index: 3;">
      <PremiumMenu />
    </section>

    <!-- Heritage & Chef Story -->
    <section id="heritage" class="perspective-section" style="position:relative; z-index: 2;">
      <HeritageStory />
    </section>

    <!-- About Section -->
    <div class="perspective-section" style="position:relative; z-index: 1;">
      <AboutSection />
    </div>

    <!-- Reviews Marquee -->
    <div class="perspective-section" style="position:relative; z-index: 0;">
      <ReviewsMarquee />
    </div>

    <footer class="perspective-section" style="position:relative; z-index: 0;">
      <div class="footer-content">
        <p>&copy; 2026 Malabar Chef Restaurant. All rights reserved.</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
.main-site {
  width: 100vw;
  background-color: var(--bg-color);
  color: var(--text-primary);
  overflow-x: hidden;
}

.navbar {
  position: fixed;
  top: 1rem;
  left: 50%;
  transform: translateX(-50%);
  width: 90%;
  max-width: 1200px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
  border-radius: 50px;
  z-index: 100;
  transition: all 0.3s;
}

.nav-logo-img {
  height: 45px;
  object-fit: contain;
  transition: transform 0.3s;
}

.nav-logo-img:hover {
  transform: scale(1.05);
}

.nav-links {
  list-style: none;
  display: flex;
  gap: 2.5rem;
  align-items: center;
}

.nav-links a {
  text-decoration: none;
  color: var(--text-primary);
  font-weight: 600;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: var(--accent-1);
}

.footer-content {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--text-secondary);
  font-family: var(--font-body);
  font-size: 0.9rem;
}
</style>
