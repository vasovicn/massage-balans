<template>
    <router-link :to="{ name: 'HomeView' }">Home</router-link>
      <!-- This is all today and future reservations -->
      <div v-for="reservationDate in sortedReservationsDates.filter(x => Date.parse(x) >= Date.parse(currentDate))" :key="reservationDate.id" style="border:1px solid;min-height:50px;">
        <h3>{{reservationDate}}</h3>
        <div v-for="reservation in this.reservations.filter(x => x.date === reservationDate)" :key="reservation">
          <div style="border:1px solid">
            {{reservation.date}}
            {{reservation.time}}
            {{reservation.length}}
            {{reservation.type}}
          </div>
        </div>
      </div>
      <div @click="togglePastReservations"  style="border:1px solid;cursor:pointer;background-color:gray;max-width: 450px;">
        <h5 style="margin: auto;">Past Reservations</h5>
        <div v-if="pastReservations">
          <div v-for="reservationDate in sortedReservationsDates.filter(x => Date.parse(x) < Date.parse(currentDate))" :key="reservationDate.id" style="border:1px solid;min-height:50px">
            <h3>{{reservationDate}}</h3>
            <div v-for="reservation in this.reservations.filter(x => x.date === reservationDate)" :key="reservation">
              <div style="border:1px solid">
                {{reservation.date}}
                {{reservation.time}}
                {{reservation.length}}
                {{reservation.type}}
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
    
<script>   
export default {
      name: 'BackendView',
      data() {
        return {
            reservations: [],
            sortedReservationsDates: [],
            pastReservations: false
        }
      },
      created() {
        this.$store.dispatch('fetchAllReservations').then(this.reservations = this.$store.state.reservations)
    },
    computed: {
      currentDate() {
        const current = new Date();
        const currentDate = `${current.getFullYear()}-${current.getMonth()+1}-${current.getDate()}`;
        console.log(currentDate)
        return currentDate;
      }
    },
    methods: {
      togglePastReservations() {
        this.pastReservations = !this.pastReservations
      }
    },
    mounted() {
      this.reservations = this.$store.state.reservations

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
    