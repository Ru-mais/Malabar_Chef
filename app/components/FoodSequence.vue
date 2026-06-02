<script setup>
import { onMounted } from 'vue'
import gsap from 'gsap'

const emit = defineEmits(['animation-complete'])

onMounted(() => {
  const tl = gsap.timeline({ 
    defaults: { ease: 'power3.out' },
    onComplete: () => {
      // Hold the final logo briefly, then tell parent to hide this sequence
      setTimeout(() => {
        emit('animation-complete')
      }, 500)
    }
  })

  // 1. Initial State: hide everything
  gsap.set('.plate', { opacity: 0, scale: 0.8, y: 50 })
  gsap.set('.porotta', { opacity: 0, y: -500, rotation: -45, scale: 0.9 })
  gsap.set('.curry', { opacity: 0, scale: 0.1, y: -200 })
  gsap.set('.steam', { opacity: 0, y: 20 })
  gsap.set('.final-logo', { opacity: 0, scale: 0.8, display: 'none' })

  // 2. The Animation Sequence
  // Wait a moment before starting
  tl.delay(0.2)
    
    // Plate fades in
    .to('.plate', { opacity: 1, scale: 1, y: 0, duration: 0.5 })
    
    // Porotta falls down with a bounce
    .to('.porotta', { opacity: 1, y: 0, rotation: 0, duration: 0.6, ease: 'bounce.out' }, '-=0.1')
    
    // Beef curry splats on top
    .to('.curry', { opacity: 1, scale: 0.9, y: 0, duration: 0.4, ease: 'back.out(1.7)' }, '+=0.1')
    
    // Steam rises from the food
    .to('.steam', { opacity: 0.6, y: -50, duration: 1, ease: 'power1.out' })
    .to('.steam', { opacity: 0, y: -100, duration: 1, ease: 'power1.in' }, '-=0.5')

    // 3. Transformation to Restaurant Name
    // Fade out the food
    .to(['.plate', '.porotta', '.curry'], { opacity: 0, scale: 1.2, duration: 0.6, stagger: 0.05 }, '+=0.2')
    
    // Fade in the logo
    .set('.final-logo', { display: 'block' })
    .to('.final-logo', { opacity: 1, scale: 1, duration: 0.8, ease: 'power2.out' })
})
</script>

<template>
  <div class="food-container">
    <div class="food-wrapper">
      <img src="/images/plate.png" class="food-layer plate" alt="Empty Plate" />
      <img src="/images/porotta.png" class="food-layer porotta" alt="Kerala Porotta" />
      <img src="/images/curry.png" class="food-layer curry" alt="Beef Curry" />
      
      <!-- CSS Steam Effect -->
      <div class="steam-container">
        <div class="steam steam-1"></div>
        <div class="steam steam-2"></div>
        <div class="steam steam-3"></div>
      </div>
      
      <!-- Final Logo Transformation -->
      <div class="final-logo">
        <h1>Malabar <span class="text-gradient">Chef</span></h1>
      </div>
    </div>
  </div>
</template>

<style scoped>
.food-container {
  position: relative;
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  background: var(--bg-color);
}

.food-wrapper {
  position: relative;
  width: 500px;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.food-layer {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: contain;
  pointer-events: none;
}

.porotta {
  transform-origin: center;
}

.curry {
  z-index: 10;
}

.steam-container {
  position: absolute;
  top: -50px;
  width: 100%;
  height: 200px;
  z-index: 20;
  display: flex;
  justify-content: center;
  gap: 20px;
  pointer-events: none;
}

.steam {
  width: 30px;
  height: 100px;
  background: linear-gradient(to top, rgba(var(--accent-1-rgb),0) 0%, rgba(200,200,200,0.8) 50%, rgba(var(--accent-1-rgb),0) 100%);
  border-radius: 50%;
  filter: blur(8px);
}

.steam-1 { margin-top: 20px; }
.steam-2 { margin-top: -10px; }
.steam-3 { margin-top: 30px; }

.final-logo {
  position: absolute;
  z-index: 50;
  text-align: center;
}

.final-logo h1 {
  font-size: 5rem;
  font-weight: 800;
  margin: 0;
  color: var(--text-primary);
  text-shadow: 0 4px 20px rgba(230, 57, 70, 0.2);
}
</style>
