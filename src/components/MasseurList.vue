<template>
    <div class="band">
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
  .band {
  /* width: 90%; */
  /* max-width: 1240px; */
  margin: 0 auto;
  display: block;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  gap: 10px;
  padding:20px;
}

@media (min-width: 30em) {
  .band {
    grid-template-columns: 1fr 1fr;
  }
}

@media (min-width: 60em) {
  .band {
    grid-template-columns: repeat(4, 1fr);
  }
}
  </style>
  