<script setup>
import { onMounted, onUnmounted } from 'vue'
import gsap from 'gsap'

onMounted(() => {
  const cursor = document.querySelector('.custom-cursor')
  
  const moveCursor = (e) => {
    gsap.to(cursor, {
      x: e.clientX,
      y: e.clientY,
      duration: 0.2,
      ease: 'power2.out'
    })
  }

  const hoverElements = document.querySelectorAll('a, button, .carousel-card, .interactive-card')
  
  const addHover = () => cursor.classList.add('cursor-hover')
  const removeHover = () => cursor.classList.remove('cursor-hover')

  hoverElements.forEach(el => {
    el.addEventListener('mouseenter', addHover)
    el.addEventListener('mouseleave', removeHover)
  })

  window.addEventListener('mousemove', moveCursor)

  onUnmounted(() => {
    window.removeEventListener('mousemove', moveCursor)
    hoverElements.forEach(el => {
      el.removeEventListener('mouseenter', addHover)
      el.removeEventListener('mouseleave', removeHover)
    })
  })
})
</script>

<template>
  <div class="custom-cursor"></div>
</template>

<style scoped>
.custom-cursor {
  position: fixed;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
  background: white;
  border-radius: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  z-index: 99999;
  mix-blend-mode: difference;
  transition: width 0.3s, height 0.3s, background 0.3s;
}

.custom-cursor.cursor-hover {
  width: 80px;
  height: 80px;
  background: rgba(var(--accent-1-rgb), 0.8);
}
</style>
