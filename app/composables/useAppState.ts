import { useState } from '#imports'

export const useAppState = () => {
  // Localization State
  const isArabic = useState<boolean>('isArabic', () => false)

  // Ambient UI theme glow (HSL)
  const activeTheme = useState<string>('activeTheme', () => 'hsl(38, 92%, 50%)')

  // Search & Filters
  const searchQuery = useState<string>('searchQuery', () => '')
  const activeSpice = useState<string>('activeSpice', () => 'all')

  const toggleLanguage = () => {
    isArabic.value = !isArabic.value
    if (typeof document !== 'undefined') {
      const dir = isArabic.value ? 'rtl' : 'ltr'
      document.documentElement.setAttribute('dir', dir)
      document.documentElement.lang = isArabic.value ? 'ar' : 'en'
    }
  }

  return {
    isArabic,
    activeTheme,
    searchQuery,
    activeSpice,
    toggleLanguage,
  }
}
