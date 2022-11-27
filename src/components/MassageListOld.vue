<template>
  <MassageCard v-for="(massage, index) in massages" :key="index" :massage="massage"
    @click="toggleReservation(massage.name)"
     />
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
  },
  methods: {
    toggleReservation(massage_name) { 
      if(this.$store.state.x !== massage_name) {
        this.$store.dispatch('setSelectedMassage', massage_name)
      }
    
    }
  }
}
</script>
