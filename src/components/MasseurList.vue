<template>
    <div class="band" style="position:relative">
      <MasseurCard v-for="masseur in masseurs" :key="masseur.id" :masseur="masseur"/>
    </div>
  </template>
  
  <script>
  import MasseurCard from '@/components/MasseurCard.vue'
  
  export default {
    name: 'MasseurList',
    data() {
      return {
        popupSucces: false
      }
    },
    components: {
        MasseurCard
  },
    created() {
      this.$store.dispatch('fetchmasseurs')
      .catch(error => {
        console.log(error)
      })
    },
    computed: {
      masseurs() {
        return this.$store.state.masseurs
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
  