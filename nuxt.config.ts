// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  ui: {
    prose: true
  },

  modules: [
    '@nuxt/eslint',
    '@nuxt/a11y',
    '@nuxt/fonts',
    '@nuxt/hints',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/content',
    '@nuxt/ui',
    '@netlify/nuxt'
  ]
})