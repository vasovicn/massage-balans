<template>
    <router-link :to="{ name: 'HomeView' }">Home</router-link>
      <!-- <div v-for="reservation in reservations" :key="reservation.id" style="min-height:50px">
        <div v-if="reservation.date > currentDate">
          MANJIII
        </div>
        <div class="reservations">
          {{reservation.date}}
          {{reservation.time}}
          {{reservation.length}}
        </div>
      </div> -->
      <div v-for="reservationDate in sortedReservationsDates" :key="reservationDate.id" style="border:1px solid;min-height:50px">
        {{reservationDate}}
        <div v-for="reservation in reservationsForDate(reservationDate)" :key="reservation">
            {{reservation.date}}
            {{reservation.time}}
            {{reservation.length}}
        </div>
      </div>
      <button @click="testMethod">TEST</button>
    </template>
    
<script>   
export default {
      name: 'BackendView',
      data() {
        return {
            reservations: [],
            sortedReservationsDates: []
        }
      },
      created() {
        this.$store.dispatch('fetchAllReservations').then(this.reservations = this.$store.state.reservations)
    },
    computed: {
      reservationsForDate(reservationDate){
        console.log('dsadasdasdasdasdasdasdasda')
        return this.reservations.filter(x => x.date === reservationDate)
      }
    },
    methods: {

      currentDate() {
        const current = new Date();
        const currentDate = `${current.getFullYear()}-${current.getMonth()+1}-${current.getDate()}`;
        return currentDate;
      },
      testMethod() {
        var reservationDates = []
        var reservations = this.reservations
        reservations.forEach(res => {
          if (!reservationDates.includes(res.date)) {
            reservationDates.push(res.date)
          }
        })
        const sortedAsc = reservationDates.sort(
          (objA, objB) => {
            return +new Date(objA) - +new Date(objB)
          }
        );
        this.sortedReservationsDates = sortedAsc
      }
    },
    mounted() {
      this.reservations = this.$store.state.reservations
      // const test = this.$store.state.reservations
      // U OVOM TRENUTKU JOS UVEK NIJE GOTOV POZIV IZ LINIJE 24

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
    