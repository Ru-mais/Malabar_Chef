<script setup>
import { onMounted, ref } from 'vue'
import gsap from 'gsap'
import { ScrollTrigger } from 'gsap/ScrollTrigger'

const svgRefs = ref([])
const setSvgRef = (el) => {
  if (el) svgRefs.value.push(el)
}

onMounted(() => {
  gsap.registerPlugin(ScrollTrigger)

  // 1. Animate the Chef Profile
  gsap.from('.chef-text-block > *', {
    scrollTrigger: {
      trigger: '.heritage-section',
      start: 'top 75%',
    },
    y: 50,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: 'power3.out'
  })

  // 2. Animate the Signature writing itself
  const sigPath = document.querySelector('.signature-path')
  if (sigPath) {
    const length = sigPath.getTotalLength()
    gsap.set(sigPath, { strokeDasharray: length, strokeDashoffset: length })
    gsap.to(sigPath, {
      scrollTrigger: {
        trigger: '.chef-signature',
        start: 'top 85%'
      },
      strokeDashoffset: 0,
      duration: 2.5,
      ease: 'power2.inOut',
      delay: 0.5
    })
  }

  // 3. Complex SVGator/Jitter style Timeline Animation
  const timelineItems = document.querySelectorAll('.timeline-item')
  
  timelineItems.forEach((item, i) => {
    // Reveal the item text
    gsap.from(item.querySelector('.tl-content'), {
      scrollTrigger: {
        trigger: item,
        start: 'top 85%'
      },
      x: 30,
      opacity: 0,
      duration: 0.8,
      ease: 'back.out(1.7)'
    })

    // Jitter-style SVG Icon Animation (Draw + Pop + Float)
    const icon = item.querySelector('.tl-icon svg')
    const paths = icon.querySelectorAll('path')
    
    paths.forEach(p => {
      const len = p.getTotalLength()
      gsap.set(p, { strokeDasharray: len, strokeDashoffset: len })
    })

    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: item,
        start: 'top 85%'
      }
    })

    // Draw the paths (SVGator drawing effect)
    tl.to(paths, {
      strokeDashoffset: 0,
      duration: 1.5,
      stagger: 0.2,
      ease: 'power2.out'
    })
    
    // Jitter Pop
    tl.to(icon, {
      scale: 1.15,
      rotate: i % 2 === 0 ? 10 : -10,
      duration: 0.3,
      ease: 'back.out(3)'
    }, "-=0.5")
    
    tl.to(icon, {
      scale: 1,
      rotate: 0,
      duration: 0.4,
      ease: 'power2.out'
    })
  })
})
</script>

<template>
  <section class="heritage-section">
    <div class="heritage-container">
      
      <!-- Left: The Chef -->
      <div class="chef-column">
        <div class="chef-text-block">
          <span class="sub-label">The Mastermind</span>
          <h2 class="section-title">Chef <br> Abdul Rahman</h2>
          <p class="chef-bio">
            With over 30 years mastering the fire of the Dum, Chef Abdul brings the unwritten recipes of the Malabar coast directly to Dammam. Every dish is a testament to heritage, slow-cooked to absolute perfection.
          </p>
          
          <div class="chef-signature">
            <p class="script-font">Abdul Rahman</p>
            <svg width="200" height="60" viewBox="0 0 200 60" fill="none" class="signature-svg">
              <path class="signature-path" d="M10,40 C30,10 50,50 70,30 S90,10 110,40 S130,50 150,20 S170,10 190,40" stroke="var(--accent-1)" stroke-width="2" stroke-linecap="round" fill="none"/>
            </svg>
          </div>
        </div>
      </div>

      <!-- Right: The Heritage Timeline -->
      <div class="timeline-column">
        <h3 class="timeline-title">The Culinary Journey</h3>
        
        <div class="timeline">
          <!-- Step 1 -->
          <div class="timeline-item">
            <div class="tl-icon glass-panel">
              <!-- Iconsax style Flame/Dum Pot -->
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22C17.5228 22 22 17.5228 22 12C22 6.47715 17.5228 2 12 2C6.47715 2 2 6.47715 2 12C2 17.5228 6.47715 22 12 22Z"/>
                <path d="M8 14C8 14 9.5 16 12 16C14.5 16 16 14 16 14"/>
                <path d="M12 7V12"/>
              </svg>
            </div>
            <div class="tl-content">
              <h4>The Art of Dum</h4>
              <p>Slow-cooked in copper pots sealed with wheat dough, locking in the essential spice oils.</p>
            </div>
          </div>

          <!-- Step 2 -->
          <div class="timeline-item">
            <div class="tl-icon glass-panel">
              <!-- Iconsax style Star Anise / Spice -->
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 3L14.5 9.5L21 12L14.5 14.5L12 21L9.5 14.5L3 12L9.5 9.5L12 3Z"/>
              </svg>
            </div>
            <div class="tl-content">
              <h4>Organic Malabar Spices</h4>
              <p>Hand-ground daily. We source our cardamom and black pepper directly from Kerala.</p>
            </div>
          </div>

          <!-- Step 3 -->
          <div class="timeline-item">
            <div class="tl-icon glass-panel">
              <!-- Iconsax style Layers / Porotta -->
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                <path d="M4 8H20"/>
                <path d="M4 16H20"/>
                <path d="M7 12H17"/>
              </svg>
            </div>
            <div class="tl-content">
              <h4>The 50-Layer Porotta</h4>
              <p>Hand-patted and stretched to create microscopic, buttery layers that peel apart effortlessly.</p>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
</template>

<style scoped>
.heritage-section {
  width: 100vw;
  padding: 8rem 5vw;
  background-color: var(--bg-color);
  position: relative;
  overflow: hidden;
}

.heritage-container {
  max-width: 1200px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

@media (max-width: 900px) {
  .heritage-container {
    grid-template-columns: 1fr;
    gap: 5rem;
  }
}

.sub-label {
  font-family: var(--font-body);
  font-size: 0.9rem;
  letter-spacing: 4px;
  text-transform: uppercase;
  color: var(--accent-1);
  margin-bottom: 1rem;
  display: inline-block;
}

.section-title {
  font-family: var(--font-heading);
  font-size: 4.5rem;
  line-height: 1.1;
  color: var(--text-primary);
  margin-bottom: 2rem;
}

.chef-bio {
  font-family: var(--font-body);
  color: var(--text-secondary);
  font-size: 1.1rem;
  line-height: 1.8;
  margin-bottom: 3rem;
  max-width: 90%;
}

.chef-signature {
  position: relative;
}

.chef-signature p {
  font-size: 4rem;
  color: var(--text-primary);
  opacity: 0.9;
  position: absolute;
  top: -20px;
  left: 20px;
  z-index: 2;
}

.signature-svg {
  position: relative;
  z-index: 1;
  opacity: 0.3;
}

/* Timeline Styles */
.timeline-title {
  font-family: var(--font-heading);
  font-size: 2.5rem;
  color: var(--text-primary);
  margin-bottom: 3rem;
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: 3rem;
  position: relative;
}

.timeline::before {
  content: '';
  position: absolute;
  top: 0;
  left: 30px;
  width: 1px;
  height: 100%;
  background: rgba(var(--accent-1-rgb), 0.2);
}

.timeline-item {
  display: flex;
  gap: 2rem;
  position: relative;
  z-index: 2;
}

.tl-icon {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  background: var(--bg-color); /* Overwrite glass-panel background for contrast */
  border: 1px solid rgba(var(--accent-1-rgb), 0.3);
  box-shadow: 0 10px 20px rgba(var(--accent-1-rgb), 0.05);
  color: var(--accent-1);
}

.tl-icon svg {
  width: 28px;
  height: 28px;
}

.tl-content {
  padding-top: 0.5rem;
}

.tl-content h4 {
  font-family: var(--font-heading);
  font-size: 1.6rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.tl-content p {
  font-family: var(--font-body);
  color: var(--text-secondary);
  font-size: 1rem;
  line-height: 1.6;
}
</style>
