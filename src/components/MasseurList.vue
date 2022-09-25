<template>
    <h1 style="text-align:center">Maseri</h1>
    <div class="masseuers">
      <MasseurCard v-for="masseur in masseuers" :key="masseur.id" :masseur="masseur"/>
    </div>
  </template>
  
  <script>
  import MasseurCard from '@/components/MasseurCard.vue'
  
  export default {
    name: 'MasseurList',
    components: {
        MasseurCard
  },
    created() {
      this.$store.dispatch('fetchMasseuers')
      .catch(error => {
        console.log(error)
      })
    },
    computed: {
      masseuers() {
        return this.$store.state.masseuers
      }
    }
  }
  </script>
  
  <style scoped>
  .masseuers {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  </style>
  