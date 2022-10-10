<template>
  <MassageCard v-for="massage in massages" :key="massage" :massage="massage" />  
</template>

<script>
import MassageCard from '@/components/MassageCard.vue'

export default {
  name: 'MassageList',
  components: {
    MassageCard
    },
  created() {
    this.$store.dispatch('getMassagesDjango')
        .catch(error => {
          console.log(error)
        })
  },
  computed: {
    massages() {
      return this.$store.state.massages
    }
  }
}
</script>

<style scoped>
</style>
