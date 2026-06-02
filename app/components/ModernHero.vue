<script setup>
import { onMounted } from 'vue'
import gsap from 'gsap'

onMounted(() => {
  gsap.from('.hero-title-line', {
    y: 150,
    opacity: 0,
    duration: 1.5,
    stagger: 0.2,
    ease: 'power4.out',
    delay: 0.2
  })
  
  gsap.from('.hero-subtitle', {
    opacity: 0,
    y: 20,
    duration: 1,
    delay: 1.0
  })

  // Marquee animation
  gsap.to('.marquee-text', {
    xPercent: -50,
    ease: "none",
    duration: 25,
    repeat: -1
  })
})
</script>

<template>
  <section class="modern-hero">
    <div class="hero-marquee">
      <div class="marquee-track">
        <h1 class="marquee-text">AUTHENTIC MALABAR TASTE • PREMIUM DINING • AUTHENTIC MALABAR TASTE • PREMIUM DINING • </h1>
      </div>
    </div>
    
    <div class="hero-content">
      <div class="title-wrapper">
        <h1 class="hero-title">
          <span class="script-font decorative-script">The finest</span>
          <span class="hero-title-line">ELEVATE</span>
          <span class="hero-title-line text-gradient">YOUR</span>
          <span class="hero-title-line">TASTE</span>
        </h1>
      </div>
      <p class="hero-subtitle">An Award-Winning Culinary Journey Through Kerala.</p>
      
      <div class="hero-image-container">
        <!-- Floating 3D Plate Image -->
        <img src="/images/plate.png" alt="Signature Dish" class="floating-hero-image" />
      </div>
    </div>
  </section>
</template>

<style scoped>
.modern-hero {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  background: var(--bg-color);
}

.hero-marquee {
  position: absolute;
  top: 50%;
  left: 0;
  width: 100%;
  transform: translateY(-50%);
  z-index: 0;
  opacity: 0.03;
  pointer-events: none;
}

.marquee-track {
  display: flex;
  width: 200%;
}

.marquee-text {
  font-size: 15vw;
  font-weight: 900;
  white-space: nowrap;
  font-family: var(--font-heading);
  text-transform: uppercase;
}

.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.title-wrapper {
  overflow: hidden;
}

.hero-title {
  font-size: 9rem;
  font-weight: 900;
  line-height: 0.9;
  letter-spacing: -2px;
  text-transform: uppercase;
  font-family: var(--font-heading);
  display: flex;
  flex-direction: column;
}

.hero-title-line {
  display: block;
}

.decorative-script {
  font-size: 4rem;
  display: block;
  margin-bottom: -2rem;
  transform: rotate(-5deg) translateX(-10%);
  text-transform: none;
  letter-spacing: 0;
  text-shadow: 0 5px 15px rgba(0,0,0,0.5);
  z-index: 5;
}

.hero-subtitle {
  margin-top: 2rem;
  font-size: 1.5rem;
  font-family: var(--font-body);
  color: var(--text-secondary);
  letter-spacing: 5px;
  text-transform: uppercase;
}

.hero-image-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: -1;
  width: 600px;
  height: 600px;
  pointer-events: none;
}

.floating-hero-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  animation: float 6s ease-in-out infinite;
  filter: drop-shadow(0 30px 50px rgba(0,0,0,0.9));
}

@keyframes float {
  0% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-30px) rotate(5deg); }
  100% { transform: translateY(0px) rotate(0deg); }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 4rem;
  }
  .hero-image-container {
    width: 300px;
    height: 300px;
  }
}
</style>
