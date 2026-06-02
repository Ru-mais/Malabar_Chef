<script setup>
import { onMounted } from 'vue'
import gsap from 'gsap'

const reviews = [
  { name: "Ahmed K.", avatar: "https://loremflickr.com/100/100/man,face/all?lock=1", guide: "Local Guide · 45 reviews", text: "The absolute best Kannur Dum Biryani in Dammam! The flavors are incredibly authentic and the meat falls right off the bone." },
  { name: "Sarah Al-F.", avatar: "https://loremflickr.com/100/100/woman,face/all?lock=2", guide: "Local Guide · 12 reviews", text: "A hidden gem on Prince Talal Street. The ambiance is premium and their authentic Malabar tea is an absolute must-have after your meal." },
  { name: "Rahul M.", avatar: "https://loremflickr.com/100/100/man,face/all?lock=3", guide: "1 review", text: "Premium quality, amazing ambiance, and the beef kondattam took me straight back home to Kerala." },
  { name: "Fatima R.", avatar: "https://loremflickr.com/100/100/woman,face/all?lock=4", guide: "Local Guide · 89 reviews", text: "Five stars! The service is top notch. Finding authentic Malabar food in Dammam of this quality is rare. Highly recommended." },
  { name: "John D.", avatar: "https://loremflickr.com/100/100/man,face/all?lock=5", guide: "Local Guide · 23 reviews", text: "The Falooda here is out of this world. Great dining experience on Prince Talal St. Will definitely be coming back." }
]

// Duplicate reviews to make the infinite scroll seamless
const duplicatedReviews = [...reviews, ...reviews]

onMounted(() => {
  gsap.to('.marquee-track', {
    xPercent: -50,
    ease: "none",
    duration: 35,
    repeat: -1
  })
})
</script>

<template>
  <div class="reviews-section fade-section">
    <div class="marquee-container">
      <div class="marquee-track">
        <div 
          v-for="(review, index) in duplicatedReviews" 
          :key="index"
          class="review-card glass-panel"
        >
          <div class="review-header">
            <img :src="review.avatar" class="avatar" alt="Reviewer" loading="lazy" />
            <div class="reviewer-info">
              <span class="review-author">{{ review.name }}</span>
              <span class="local-guide">{{ review.guide }}</span>
            </div>
            <div class="google-icon">
              <svg viewBox="0 0 24 24" width="24" height="24">
                <path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/>
                <path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.16v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/>
                <path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.16C1.43 8.55 1 10.22 1 12s.43 3.45 1.16 4.93l3.68-2.84z" fill="#FBBC05"/>
                <path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.16 7.07l3.68 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/>
              </svg>
            </div>
          </div>
          
          <div class="stars">
            <svg v-for="i in 5" :key="i" width="16" height="16" viewBox="0 0 24 24" fill="#FBBC05" stroke="#FBBC05" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
          </div>
          <p class="review-text">"{{ review.text }}"</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.reviews-section {
  padding: 4rem 0 8rem 0;
  background: var(--bg-color);
  overflow: hidden;
  position: relative;
  z-index: 2;
}

.marquee-container {
  width: 100vw;
  overflow: hidden;
  position: relative;
}

/* Gradient masks for edges */
.marquee-container::before,
.marquee-container::after {
  content: '';
  position: absolute;
  top: 0; bottom: 0;
  width: 15vw;
  z-index: 10;
  pointer-events: none;
}
.marquee-container::before {
  left: 0;
  background: linear-gradient(to right, var(--bg-color), transparent);
}
.marquee-container::after {
  right: 0;
  background: linear-gradient(to left, var(--bg-color), transparent);
}

.marquee-track {
  display: flex;
  gap: 2rem;
  width: max-content;
  padding: 1rem 2rem;
}

.review-card {
  width: 450px;
  padding: 2.5rem;
  background: linear-gradient(145deg, rgba(var(--accent-1-rgb),0.03), rgba(0,0,0,0.5));
  border: 1px solid rgba(var(--accent-1-rgb),0.05);
  border-radius: 24px;
  flex-shrink: 0;
  box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.review-header {
  display: flex;
  align-items: center;
  gap: 1rem;
  margin-bottom: 1.5rem;
  position: relative;
}

.avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
}

.reviewer-info {
  display: flex;
  flex-direction: column;
}

.review-author {
  font-family: var(--font-body);
  color: #fff;
  font-weight: 700;
  font-size: 1.1rem;
}

.local-guide {
  font-family: var(--font-body);
  color: var(--text-secondary);
  font-size: 0.85rem;
}

.google-icon {
  position: absolute;
  right: 0;
  top: 0;
}

.stars {
  display: flex;
  gap: 0.2rem;
  margin-bottom: 1rem;
}

.review-text {
  font-family: var(--font-heading);
  font-size: 1.2rem;
  line-height: 1.6;
  color: #e0e0e0;
  margin-bottom: 0;
}
</style>
