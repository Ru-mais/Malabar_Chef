<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import gsap from 'gsap'
import rawMenuData from '../data/menu.json'

// Create a "Top Selling" category dynamically
const topSellingItems = [
  rawMenuData.find(c => c.category === 'BIRYANI')?.items[0],
  rawMenuData.find(c => c.category === 'FALOODA')?.items[0],
  rawMenuData.find(c => c.category === 'CHICKEN DISHES')?.items[0],
  rawMenuData.find(c => c.category === 'HOT & COOL')?.items[0],
].filter(Boolean)

const menuData = [
  { category: 'Top Selling', items: topSellingItems, color: '#e0b93e' },
  ...rawMenuData
]

const activeCategory = ref(menuData[0].category)

const activeItems = computed(() => {
  const category = menuData.find(c => c.category === activeCategory.value)
  return category ? category.items : []
})

const selectCategory = async (catName) => {
  activeCategory.value = catName
  await nextTick()
  init3DEffects()
  
  // Simple list entrance animation
  gsap.from('.item-card', {
    y: 30,
    opacity: 0,
    duration: 0.5,
    stagger: 0.05,
    ease: 'power2.out'
  })
}

const init3DEffects = () => {
  const cards = document.querySelectorAll('.item-card')
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect()
      const x = e.clientX - rect.left
      const y = e.clientY - rect.top
      const centerX = rect.width / 2
      const centerY = rect.height / 2
      const rotateX = ((y - centerY) / centerY) * -15
      const rotateY = ((x - centerX) / centerX) * 15

      gsap.to(card, {
        rotateX,
        rotateY,
        scale: 1.02,
        duration: 0.4,
        ease: 'power2.out',
        transformPerspective: 1000
      })
    })

    card.addEventListener('mouseleave', () => {
      gsap.to(card, {
        rotateX: 0,
        rotateY: 0,
        scale: 1,
        duration: 0.4,
        ease: 'power2.out'
      })
    })
  })
}

onMounted(() => {
  init3DEffects()
})
</script>

<template>
  <div class="app-style-menu">
    <div class="menu-header">
      <h2 class="text-gradient">Our Menu</h2>
    </div>

    <div class="menu-layout">
      <!-- Sidebar / Topbar Navigation -->
      <nav class="category-nav">
        <div class="nav-inner">
          <button 
            v-for="(cat, index) in menuData" 
            :key="index"
            class="cat-btn"
            :class="{ active: activeCategory === cat.category }"
            @click="selectCategory(cat.category)"
          >
            {{ cat.category }}
          </button>
        </div>
      </nav>

      <!-- Items List -->
      <div class="menu-items-list">
        <div 
          v-for="(item, index) in activeItems" 
          :key="index"
          class="item-card"
        >
          <div class="card-image-wrap">
            <img :src="item.image" :alt="item.name" class="item-img" loading="lazy" />
          </div>
          
          <div class="card-details">
            <div class="item-details">
              <h4 class="item-name">{{ item.name }}</h4>
              <div class="item-meta">
                <p class="item-price">{{ item.price }} SAR</p>
                <p class="item-calories" v-if="item.cal">🔥 {{ item.cal }} Cal</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.app-style-menu {
  width: 100vw;
  background: var(--bg-color);
  padding: 6rem 5vw;
  position: relative;
  z-index: 2;
  font-family: var(--font-body);
}

.menu-header {
  margin-bottom: 4rem;
  text-align: center;
}

.menu-header h2 {
  font-size: 5rem;
  font-family: var(--font-heading);
  font-weight: 900;
  letter-spacing: -2px;
}

.menu-layout {
  display: flex;
  gap: 5rem;
  max-width: 1200px;
  margin: 0 auto;
}

/* Category Navigation */
.category-nav {
  flex: 0 0 280px;
  position: sticky;
  top: 100px;
  height: max-content;
  max-height: 80vh;
  overflow-y: auto;
}

.category-nav::-webkit-scrollbar {
  display: none;
}

.nav-inner {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.cat-btn {
  background: transparent;
  border: 1px solid transparent;
  color: var(--text-secondary);
  font-size: 1.2rem;
  font-weight: 600;
  text-align: left;
  padding: 1.2rem 1.8rem;
  border-radius: 16px;
  transition: all 0.3s;
  cursor: none; /* custom cursor */
}

.cat-btn:hover {
  color: #fff;
  background: rgba(var(--accent-1-rgb),0.03);
  border-color: rgba(var(--accent-1-rgb),0.1);
  transform: translateX(10px);
}

.cat-btn.active {
  color: #000;
  background: var(--accent-gradient);
  box-shadow: 0 10px 20px rgba(var(--accent-1-rgb), 0.2);
  transform: translateX(10px);
}

/* Items List */
.menu-items-list {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.item-card {
  position: relative;
  display: flex;
  align-items: center;
  background: rgba(var(--accent-1-rgb),0.02);
  padding: 1.5rem;
  border-radius: 24px;
  gap: 2rem;
  box-shadow: 0 15px 35px rgba(0,0,0,0.6);
  border: 1px solid rgba(var(--accent-1-rgb), 0.15); /* Subtle gold border */
  transform-style: preserve-3d;
  will-change: transform;
  position: relative;
  overflow: hidden;
}

.item-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(circle at 100% 0%, rgba(201,162,39,0.05) 0%, transparent 50%);
  pointer-events: none;
}

.card-image-wrap {
  width: 140px;
  height: 140px;
  border-radius: 16px;
  overflow: hidden;
  flex-shrink: 0;
  transform: translateZ(30px);
  position: relative;
  box-shadow: 0 10px 20px rgba(0,0,0,0.5);
}

.item-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.card-details {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  transform: translateZ(40px);
}

.title-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.item-name {
  font-family: var(--font-heading);
  font-size: 1.4rem;
  color: var(--text-primary);
  margin-bottom: 0.5rem;
}

.item-meta {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.item-price {
  font-family: var(--font-body);
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--accent-1);
}

.item-calories {
  font-family: var(--font-body);
  font-size: 0.85rem;
  font-weight: 500;
  color: var(--text-secondary);
  background: rgba(var(--accent-1-rgb), 0.1);
  padding: 0.2rem 0.6rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
}

/* Mobile Layout */
@media (max-width: 768px) {
  .menu-layout {
    flex-direction: column;
    gap: 2rem;
  }
  
  .category-nav {
    flex: none;
    position: sticky;
    top: 70px;
    z-index: 50;
    margin: 0 -5vw;
    padding: 0 5vw;
    background: var(--bg-color);
  }
  
  .nav-inner {
    flex-direction: row;
    overflow-x: auto;
    padding-bottom: 1rem;
  }
  
  .cat-btn {
    white-space: nowrap;
    text-align: center;
    padding: 0.8rem 1.2rem;
  }

  .cat-btn:hover, .cat-btn.active {
    transform: none;
  }
  
  .item-card {
    padding: 1rem;
    gap: 1rem;
    flex-direction: column;
    align-items: flex-start;
  }

  .card-image-wrap {
    width: 100%;
    height: 180px;
  }

  .add-btn {
    position: absolute;
    bottom: 1rem;
    right: 1rem;
  }
}
</style>
