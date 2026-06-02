<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'
import offersData from '../data/offers.json'

const offers = ref(offersData)
const currentIndex = ref(0)
let autoplayInterval

onMounted(async () => {
  gsap.registerPlugin(ScrollTrigger)

  // Start 3D interaction observer
  const container = document.querySelector('.carousel-container')
  if (container) {
    ScrollTrigger.create({
      trigger: container,
      start: 'top 80%',
      onEnter: () => {
        autoplayInterval = setInterval(nextSlide, 4000)
      }
    })
  }
})

onUnmounted(() => {
  if (autoplayInterval) {
    clearInterval(autoplayInterval)
  }
})

const nextSlide = () => {
  if (offers.value.length === 0) return
  currentIndex.value = (currentIndex.value + 1) % offers.value.length
}

const prevSlide = () => {
  if (offers.value.length === 0) return
  currentIndex.value = (currentIndex.value - 1 + offers.value.length) % offers.value.length
}

const setSlide = (index) => {
  currentIndex.value = index
}

// Calculate the 3D style for each card based on its distance from the currentIndex
const getCardStyle = (index) => {
  const total = offers.value.length
  // Calculate relative distance (-2, -1, 0, 1, 2)
  let diff = index - currentIndex.value
  
  // Handle wrapping
  if (diff > Math.floor(total / 2)) diff -= total
  if (diff < -Math.floor(total / 2)) diff += total

  const absDiff = Math.abs(diff)
  const isCenter = diff === 0
  
  // Base transform values
  let translateX = diff * 45 // Percentage of width
  let translateZ = isCenter ? 150 : -absDiff * 150
  let rotateY = diff * -35 // Degrees
  let opacity = isCenter ? 1 : 1 - (absDiff * 0.4)
  let scale = isCenter ? 1 : 1 - (absDiff * 0.15)
  
  // Hide cards that are too far away
  if (absDiff > 2) {
    opacity = 0
    translateZ = -500
  }

  return {
    transform: `translateX(${translateX}%) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale})`,
    opacity: opacity,
    zIndex: 10 - absDiff,
    pointerEvents: isCenter ? 'auto' : 'none'
  }
}

onMounted(() => {
  autoplayInterval = setInterval(nextSlide, 4000)
})

onUnmounted(() => {
  clearInterval(autoplayInterval)
})
</script>

<template>
  <div class="offers-carousel-section">
    <div class="carousel-header">
      <h2 class="text-gradient">Exclusive Offers</h2>
      <p>Discover our latest deals and chef specials</p>
    </div>

    <div class="carousel-container">
      <button class="nav-btn prev" @click="prevSlide">❮</button>
      
      <div class="carousel-3d-scene">
        <div 
          v-for="(offer, index) in offers" 
          :key="index"
          class="carousel-card glass-panel"
          :style="getCardStyle(index)"
          @click="setSlide(index)"
        >
          <div class="card-glow" :style="{ background: `radial-gradient(circle at center, ${offer.color}60 0%, transparent 70%)` }"></div>
          
          <div class="card-content">
            <div class="image-wrapper">
              <img :src="offer.image" alt="Offer Image" class="offer-image"/>
            </div>
            <div class="text-wrapper">
              <div class="offer-details">
                <h3 :style="{ color: offer.color }">{{ offer.title }}</h3>
                <p>{{ offer.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <button class="nav-btn next" @click="nextSlide">❯</button>
    </div>
    
    <div class="carousel-indicators">
      <span 
        v-for="(_, index) in offers" 
        :key="index"
        class="dot"
        :class="{ active: currentIndex === index }"
        @click="setSlide(index)"
      ></span>
    </div>
  </div>
</template>

<style scoped>
.offers-carousel-section {
  width: 100vw;
  padding: 6rem 0;
  background: var(--bg-color);
  position: relative;
  overflow: hidden;
}

.carousel-header {
  text-align: center;
  margin-bottom: 4rem;
}

.carousel-header h2 {
  font-size: 3rem;
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 2px;
}

.carousel-header p {
  color: var(--text-secondary);
  font-size: 1.2rem;
  margin-top: 0.5rem;
}

.carousel-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  width: 100%;
  height: 450px;
}

.nav-btn {
  background: rgba(var(--accent-1-rgb),0.1);
  border: 1px solid rgba(var(--accent-1-rgb),0.2);
  color: #fff;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  font-size: 1.5rem;
  cursor: pointer;
  z-index: 20;
  display: flex;
  justify-content: center;
  align-items: center;
  transition: all 0.3s ease;
  position: absolute;
}

.nav-btn:hover {
  background: rgba(var(--accent-1-rgb),0.2);
  transform: scale(1.1);
}

.nav-btn.prev {
  left: 10vw;
}

.nav-btn.next {
  right: 10vw;
}

.carousel-3d-scene {
  perspective: 1500px;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
  transform-style: preserve-3d;
}

.carousel-card {
  position: absolute;
  width: 600px;
  height: 350px;
  border-radius: 20px;
  background: rgba(20, 20, 20, 0.8);
  border: 1px solid rgba(var(--accent-1-rgb), 0.1);
  backdrop-filter: blur(20px);
  transition: transform 0.6s cubic-bezier(0.23, 1, 0.32, 1), opacity 0.6s ease, z-index 0s;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,0.6);
  cursor: pointer;
}

.card-glow {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 0;
  opacity: 0.5;
}

.card-content {
  position: relative;
  z-index: 2;
  display: flex;
  height: 100%;
  padding: 2rem;
  align-items: center;
  gap: 2rem;
}

.image-wrapper {
  flex: 1;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.offer-image {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 20px 20px rgba(0,0,0,0.5));
  transform: translateZ(30px);
}

.text-wrapper {
  flex: 1.2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  transform: translateZ(40px);
}

.text-wrapper h3 {
  font-size: 2rem;
  font-weight: 800;
  margin-bottom: 1rem;
  line-height: 1.1;
}

.offer-details p {
  font-family: var(--font-body);
  font-size: 1.1rem;
  line-height: 1.6;
  color: var(--text-secondary);
}

.carousel-nav {
  margin-top: 2rem;
}

.dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(var(--accent-1-rgb),0.2);
  cursor: pointer;
  transition: all 0.3s ease;
}

.dot.active {
  background: var(--accent-1);
  transform: scale(1.3);
}

@media (max-width: 768px) {
  .carousel-card {
    width: 320px;
    height: 400px;
  }
  .card-content {
    flex-direction: column;
    text-align: center;
  }
  .text-wrapper {
    align-items: center;
  }
  .nav-btn {
    display: none;
  }
}
</style>
