<template>
    <router-link :to="{ name: 'HomeView' }">Home</router-link>
      <!-- This is all today and future reservations -->
      <div v-for="reservationDate in sortedReservationsDates.filter(x => Date.parse(x) >= Date.parse(currentDate))" :key="reservationDate.id" style="border:1px solid;min-height:50px;">
        <div v-if="Date.parse(reservationDate) === Date.parse(currentDate)">
          <h3>TODAY ({{reservationDate}})</h3>
        </div>
        <div v-else>
          <h3>{{reservationDate}}</h3>
        </div>
        <div v-for="reservation in this.reservations.filter(x => x.date === reservationDate).sort(function (a, b) {return a.time.localeCompare(b.time)})" :key="reservation">
          <div style="border:1px solid">
            {{reservation.time}}
            {{reservation.length}} min
            {{reservation.type}}
          </div>
        </div>
      </div>
      <div @click="togglePastReservations"  style="border:1px solid;cursor:pointer;background-color:gray;max-width: 450px;">
        <h5 style="margin: auto;">Past Reservations</h5>
        <div v-if="pastReservations">
          <div v-for="reservationDate in sortedReservationsDates.filter(x => Date.parse(x) < Date.parse(currentDate))" :key="reservationDate.id" style="border:1px solid;min-height:50px">
            <h3>{{reservationDate}}</h3>
            <div v-for="reservation in this.reservations.filter(x => x.date === reservationDate).sort(function (a, b) {return a.time.localeCompare(b.time)})" :key="reservation">
              <div style="border:1px solid">
                {{reservation.time}}
                {{reservation.length}} min
                {{reservation.type}}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <h1>Masaze:</h1>
        <div v-for="massage in massages" :key="massage.id">
          {{massage.name}}
          <button @click="deleteMassage(massage)">delete</button>
        </div>
        <router-link :to="{ name: 'CreateNewMassage' }">add new massage</router-link>
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
        return currentDate;
      },
      massages() {
        return this.$store.state.massages
      }
    },
    methods: {
      togglePastReservations() {
        this.pastReservations = !this.pastReservations
      },
      deleteMassage(massage) {
        this.$store.dispatch('deleteMassage', massage)
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
    