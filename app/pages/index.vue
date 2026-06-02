<script setup>
import { ref } from 'vue'
import { useHead } from '#imports'
import FoodSequence from '~/components/FoodSequence.vue'
import MainSite from '~/components/MainSite.vue'

useHead({
  script: [
    {
      type: 'application/ld+json',
      children: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "Restaurant",
        "name": "Malabar Chef",
        "image": "https://malabarchef.example.com/images/signature_biryani.png",
        "description": "The best authentic Kerala Malabar food in Dammam. Famous for our flaky butter porotta and Kannur Dum Biryani.",
        "address": {
          "@type": "PostalAddress",
          "streetAddress": "Prince Talal Street",
          "addressLocality": "Dammam",
          "addressRegion": "Eastern Province",
          "addressCountry": "SA"
        },
        "servesCuisine": ["Kerala", "Malabar", "Indian", "South Indian"],
        "priceRange": "$$",
        "telephone": "+966-123-456-789", 
        "url": "https://malabarchef.example.com",
        "knowsAbout": [
          "Best Malabar food in Dammam", 
          "Kannur Dum Biryani in Saudi Arabia", 
          "Kerala Porotta in Dammam", 
          "Authentic South Indian Takeaway"
        ]
      })
    }
  ]
})

// Controls whether the splash animation is showing
const showSplash = ref(true)

const onSplashComplete = () => {
  showSplash.value = false
}
</script>

<template>
  <div>
    <!-- The Splash Screen Animation -->
    <FoodSequence v-if="showSplash" @animation-complete="onSplashComplete" />
    
    <!-- The Main Website Content -->
    <MainSite v-else />
  </div>
</template>
