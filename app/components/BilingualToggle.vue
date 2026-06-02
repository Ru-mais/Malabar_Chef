<script setup lang="ts">
import { useAppState } from '~/composables/useAppState'

const { isArabic, toggleLanguage } = useAppState()
</script>

<template>
  <button 
    class="language-switcher glass-panel" 
    @click="toggleLanguage" 
    aria-label="Toggle language"
  >
    <span 
      class="active-slider" 
      :class="{ 'slide-ar': isArabic }"
    ></span>
    <span class="lang-label" :class="{ 'active-text': !isArabic }">EN</span>
    <span class="lang-label" :class="{ 'active-text': isArabic }">عربي</span>
  </button>
</template>

<style scoped>
.language-switcher {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  width: 100px;
  height: 38px;
  border-radius: 20px;
  padding: 4px;
  cursor: pointer;
  background: var(--color-obsidian-glass);
  border: 1px solid rgba(var(--accent-1-rgb), 0.08);
  font-family: var(--font-en-head);
  font-size: 13px;
  font-weight: 700;
  overflow: hidden;
  user-select: none;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
}

.language-switcher:hover {
  border-color: var(--color-saffron);
}

.active-slider {
  position: absolute;
  top: 3px;
  left: 3px;
  width: 44px;
  height: 30px;
  background: linear-gradient(135deg, var(--color-saffron) 0%, var(--color-ginger) 100%);
  border-radius: 16px;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 1;
}

.slide-ar {
  transform: translateX(48px);
}

[dir="rtl"] .slide-ar {
  /* Nuxt coordinates swaps LTR/RTL naturally. If needed, we override */
  transform: translateX(-48px);
}

.lang-label {
  position: relative;
  width: 44px;
  text-align: center;
  z-index: 2;
  color: var(--color-ivory-dim);
  transition: color 0.3s ease;
  font-family: inherit;
}

.active-text {
  color: var(--color-obsidian-dark);
}
</style>
