// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  css: ['~/assets/css/main.css'],
  modules: ['@tresjs/nuxt'],
  devtools: { enabled: true },
  app: {
    head: {
      title: 'Malabar Chef | Premium Authentic Kerala Dining in Dammam',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { name: 'description', content: 'Experience the finest, authentic Kerala Malabar cuisine right in Dammam. Famous for our flaky butter porotta, slow-cooked Kannur Dum Biryani, and organic spices.' },
        { name: 'keywords', content: 'Malabar Chef, Dammam restaurant, Kerala cuisine, Malabar food, Dum Biryani, Porotta, Indian restaurant Dammam, Takeaway' },
        
        /* OpenGraph / Social Media Meta Tags */
        { property: 'og:title', content: 'Malabar Chef | Premium Authentic Kerala Dining' },
        { property: 'og:description', content: 'Experience the finest, authentic Kerala Malabar cuisine right in Dammam. Famous for our flaky butter porotta and Kannur Dum Biryani.' },
        { property: 'og:image', content: '/images/signature_biryani.png' },
        { property: 'og:url', content: 'https://malabarchef.example.com' },
        { property: 'og:type', content: 'website' },
        { property: 'og:locale', content: 'en_SA' },
        
        /* Twitter Cards */
        { name: 'twitter:card', content: 'summary_large_image' },
        { name: 'twitter:title', content: 'Malabar Chef | Premium Authentic Kerala Dining' },
        { name: 'twitter:description', content: 'Experience the finest, authentic Kerala Malabar cuisine right in Dammam.' },
        { name: 'twitter:image', content: '/images/signature_biryani.png' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    }
  }
})
