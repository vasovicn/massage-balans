<template>
      <div v-for="reservation in reservations" :key="reservation.id" style="min-height:50px">
        <div v-if="reservation.date > currentDate">
          MANJIII
        </div>
        <div class="reservations">
          {{reservation.date}}
          {{reservation.time}}
          {{reservation.length}}
        </div>
      </div>
      <button @click="currentDate">TEST</button>
    </template>
    
<script>   
export default {
      name: 'BackendView',
      data() {
        return {
            reservations: []
        }
      },
      created() {
        this.$store.dispatch('fetchAllReservations').then(this.reservations = this.$store.state.reservations)
    },
    methods: {
      currentDate() {
        const current = new Date();
        const currentDate = `${current.getFullYear()}-${current.getMonth()+1}-${current.getDate()}`;
        console.log(currentDate)
        return currentDate;
      }
    },
    mounted() {
      this.reservations = this.$store.state.reservations
      const test = this.$store.state.reservations
      // U OVOM TRENUTKU JOS UVEK NIJE GOTOV POZIV IZ LINIJE 24
      console.log('TEST:', test)
    }
}
</script>
    
<style scoped>
  .reservations {
    display: flex;
    flex-direction: column;
    align-items: center;
    border: 1px solid;
    max-width: 300px
  }
</style>
    