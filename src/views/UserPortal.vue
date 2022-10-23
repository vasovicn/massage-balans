<template>
  <div class="container" v-if="this.readonlyInfo && userInfo">
    <div class="card">
      <div class="card-body">
        <h5 class="card-title">{{userInfo.user.first_name}}</h5>
        <p class="card-text">{{userInfo.user.last_name}}</p>
        <p class="card-text">{{userInfo.user.email}}</p>
        <p class="card-text">{{userInfo.phone_number}}</p>
        <p class="card-text">{{userInfo.birth_date}}</p>
        <p class="card-text">{{userInfo.location}}</p>
      </div>
      <button v-if="this.readonlyInfo" @click="this.readonlyInfo = false">Edit</button>
    </div>
  </div>
  <div v-if="!this.readonlyInfo && this.userInfoForm">
    <form>
      <div class="form-group">
        <input type="text" class="form-control" placeholder="Enter your full name" v-model="this.userInfoForm.user.first_name">
      </div>
      <div class="form-group">
        <input type="email" class="form-control" placeholder="Enter email" v-model="this.userInfoForm.user.email">
      </div>
      <div class="form-group">
        <input type="text" class="form-control" placeholder="Enter phone number" v-model="this.userInfoForm.phone_number">
      </div>
      <button type="submit" class="btn btn-primary" data-dismiss="modal" aria-label="Close"
        @click="saveInfo">Save</button>
    </form>
  </div>

  <div v-for="reservationDate in sortedReservations.filter(x => Date.parse(x) >= Date.parse(currentDate))"
    :key="reservationDate" style="border:1px solid;min-height:50px;">
    <div v-if="Date.parse(reservationDate) === Date.parse(currentDate)">
      <h3>TODAY ({{reservationDate}})</h3>
    </div>
    <div v-else>
      <h3>{{reservationDate}}</h3>
    </div>
    <div
      v-for="reservation in reservations.filter(x => x.date === reservationDate).sort(function (a, b) {return a.time.localeCompare(b.time)})"
      :key="reservation.id">
      <div style="border:1px solid">
        {{reservation.time}}
        {{reservation.massage_id.length}} min
        {{reservation.massage_id.type}}
        {{reservation.massage_id.price}}
        <button @click="deleteReservation(reservation)">otkazi</button>
      </div>
    </div>
  </div>
  <div @click="togglePastReservations" style="border:1px solid;cursor:pointer;background-color:gray;max-width: 450px;">
    <h5 style="margin: auto;">Past Reservations</h5>
    <div v-if="pastReservations">
      <div v-for="reservationDate in sortedReservations.filter(x => Date.parse(x) < Date.parse(currentDate))"
        :key="reservationDate" style="border:1px solid;min-height:50px">
        <h3>{{reservationDate}}</h3>
        <div
          v-for="reservation in reservations.filter(x => x.date === reservationDate).sort(function (a, b) {return a.time.localeCompare(b.time)})"
          :key="reservation">
          <div style="border:1px solid">
            {{reservation.time}}
            {{reservation.massage_id.length}} min
            {{reservation.massage_id.type}}
            {{reservation.massage_id.price}}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
    
<script>
import axios from 'axios'

export default {
  name: 'UserPortal',
  data() {
    return {
      pastReservations: false,
      readonlyInfo: true,
      userInfoForm: null
    }
  },
  components: {
  },
  created() {
    this.$store.dispatch('userPortal').then(
      response => {
        console.log(response)
        var reservationDates = [];
        var reservations = this.$store.state.userReservations;
        reservations.forEach(res => {
          if (!reservationDates.includes(res.date)) {
            reservationDates.push(res.date);
          }
        });
        this.sortedReservations = reservationDates
      }
    )


  },
  beforeCreate() {
    this.$store.dispatch('initialToken')
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
    this.$store.dispatch('getUserInfo').then(
      response => {
        console.log(response)
        this.userInfoForm = this.$store.state.userInfo
      }
    )
  },
  methods: {
    deleteReservation(reservation) {
      this.$store.dispatch("deleteReservation", reservation);
    },
    togglePastReservations() {
      this.pastReservations = !this.pastReservations;
    },
    saveInfo() {
      this.$store.dispatch('updateInfo', this.userInfoForm)
      this.readonlyInfo = true

    }
  },
  computed: {
    reservations() {
      return this.$store.state.userReservations
    },
    currentDate() {
      const current = new Date();
      const currentDate = `${current.getFullYear()}-${current.getMonth() + 1}-${current.getDate()}`;
      return currentDate;
    },
    sortedReservations() {
      var reservationDates = [];
      var reservations = this.$store.state.userReservations;
      reservations.forEach(res => {
        if (!reservationDates.includes(res.date)) {
          reservationDates.push(res.date);
        }
      });
      return reservationDates
    },
    userInfo() {
      return this.$store.state.userInfo
    }
  }
}
</script>
    
<style scoped>
@import'~bootstrap/dist/css/bootstrap.css'
</style>
    