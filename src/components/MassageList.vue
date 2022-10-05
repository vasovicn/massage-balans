<template>
  <head>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous"/>
  </head>
      <div class="band">
        <MassageCard v-for="massage in massages" :key="massage.id" :massage="massage" />
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
  .band {
  /* width: 90%; */
  /* max-width: 1240px; */
  margin: 0 auto;
  display: column;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: auto;
  gap: 10px;
  padding:10px;
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
