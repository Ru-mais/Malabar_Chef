<script setup>
import { ref } from 'vue'
import FoodSequence from '~/components/FoodSequence.vue'
import MainSite from '~/components/MainSite.vue'

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
