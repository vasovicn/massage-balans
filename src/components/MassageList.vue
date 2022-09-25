<template>
  <h1 style="text-align:center">Masaze</h1>
  <div class="massages">
    <MassageCard v-for="massage in massages" :key="massage.id" :massage="massage"/>
  </div>
</template>

<script>
import MassageCard from '@/components/MassageCard.vue'

export default {
  name: 'MassageList',
  components: {
    MassageCard
},
  created() {
    this.$store.dispatch('fetchMassages')
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
.massages {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
