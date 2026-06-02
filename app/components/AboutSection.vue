<script setup>
import { onMounted } from 'vue'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

gsap.registerPlugin(ScrollTrigger)

onMounted(() => {
  gsap.from('.about-card', {
    scrollTrigger: {
      trigger: '.about-grid',
      start: 'top 80%',
    },
    y: 50,
    opacity: 0,
    duration: 0.8,
    stagger: 0.2,
    ease: 'power3.out'
  })
})
</script>

<template>
  <section id="about" class="about-section fade-section">
    <div class="about-container">
      <div class="section-header">
        <h2 class="text-gradient">Our Story</h2>
        <p>The true essence of Malabar, right in Dammam.</p>
      </div>

      <div class="about-grid">
        <!-- Main Image Card -->
        <div class="about-card image-card">
          <img src="https://loremflickr.com/800/800/biryani,kerala,food/all" alt="Malabar Feast" class="about-img" loading="lazy" />
          <div class="image-overlay">
            <h3>Authentic Kannur Dum Biryani</h3>
          </div>
        </div>

        <!-- Details Column -->
        <div class="about-details">
          <!-- Text Card -->
          <div class="about-card text-card glass-panel">
            <h3>The Malabar Chef</h3>
            <p>
              We bring the rich, authentic flavors of the Malabar coast directly to your table. 
              Our chefs use traditional spices and age-old recipes to craft the perfect Kannur Dum Biryani 
              and the most refreshing Malabar tea you will ever taste.
            </p>
          </div>

          <!-- Location Card -->
          <a href="https://maps.app.goo.gl/search/Prince+Talal+Street+Dammam" target="_blank" rel="noopener noreferrer" class="about-card location-card glass-panel magnetic-btn">
            <div class="icon-wrap">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
            </div>
            <div>
              <h4>Location</h4>
              <p>Prince Talal Street, Dammam</p>
            </div>
            <div class="external-icon">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="7" y1="17" x2="17" y2="7"></line><polyline points="7 7 17 7 17 17"></polyline></svg>
            </div>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.about-section {
  padding: 8rem 5vw;
  background: var(--bg-color);
  position: relative;
  z-index: 2;
}

.about-container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.section-header h2 {
  font-size: 5rem;
  font-family: var(--font-heading);
  font-weight: 900;
  letter-spacing: -2px;
}

.section-header p {
  color: var(--text-secondary);
  font-size: 1.2rem;
  letter-spacing: 2px;
  text-transform: uppercase;
  margin-top: 1rem;
}

.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
}

.about-card {
  border-radius: 24px;
  overflow: hidden;
  position: relative;
}

.image-card {
  height: 100%;
  min-height: 400px;
}

.about-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.image-card:hover .about-img {
  transform: scale(1.05);
}

.image-overlay {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  padding: 2rem;
  background: linear-gradient(to top, rgba(0,0,0,0.9), transparent);
}

.image-overlay h3 {
  font-family: var(--font-heading);
  font-size: 2rem;
  color: #fff;
}

.about-details {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.text-card {
  padding: 3rem;
  background: linear-gradient(145deg, rgba(var(--accent-1-rgb),0.03), rgba(0,0,0,0.5));
  border: 1px solid rgba(var(--accent-1-rgb),0.05);
  flex: 1;
}

.text-card h3 {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  color: var(--accent-1);
  margin-bottom: 1.5rem;
}

.text-card p {
  font-family: var(--font-body);
  color: var(--text-secondary);
  font-size: 1.1rem;
  line-height: 1.8;
}

.location-card {
  padding: 2rem;
  background: rgba(var(--accent-1-rgb), 0.05);
  border: 1px solid rgba(var(--accent-1-rgb), 0.2);
  display: flex;
  align-items: center;
  gap: 1.5rem;
  cursor: none;
  transition: all 0.3s;
  text-decoration: none;
  position: relative;
}

.location-card:hover {
  background: rgba(var(--accent-1-rgb), 0.1);
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(var(--accent-1-rgb), 0.1);
}

.external-icon {
  position: absolute;
  top: 1.5rem;
  right: 1.5rem;
  color: var(--accent-1);
  opacity: 0.5;
  transition: all 0.3s;
}

.location-card:hover .external-icon {
  opacity: 1;
  transform: translate(3px, -3px);
}

.icon-wrap {
  width: 60px;
  height: 60px;
  background: var(--accent-gradient);
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #000;
  flex-shrink: 0;
}

.location-card h4 {
  font-size: 1.2rem;
  color: #fff;
  margin-bottom: 0.3rem;
}

.location-card p {
  color: var(--text-secondary);
  font-size: 1rem;
}

@media (max-width: 768px) {
  .about-grid {
    grid-template-columns: 1fr;
  }
}
</style>
