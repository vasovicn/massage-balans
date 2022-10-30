<template>
  <div class="row" style="padding:30px">
    <div class="col-8">
      <!-- {{futureTermins}}
      <h3 :style="{color: this.futureTermins}" @click="this.futureTermins = 'green'">Pretsojeci termini</h3>|<h3 :style="{color: this.futureTermins}" @click="this.futureTermins = 'green'">Istorija masaza</h3> -->
      <div v-for="reservationDate in sortedReservations.filter(x => Date.parse(x) >= Date.parse(currentDate))"
        :key="reservationDate" style="min-height:50px;">
        <div style="margin: 20px 0;" v-if="Date.parse(reservationDate) === Date.parse(currentDate)">
          <h3>DANAS ({{ reservationDate }})</h3>
        </div>
        <div v-else style="margin: 20px 0;">
          <h3>{{ reservationDate }}</h3>
        </div>
        <div class="row">
          <div class="card" style="width: 30%; margin: 10px;"
          v-for="reservation in reservations.filter(x => x.date === reservationDate).sort(function (a, b) { return a.time.localeCompare(b.time) })"
          :key="reservation.id">
          <div class="card-header" style="text-align: center; background-color: #5BD5C9">
            {{reservation.massage_id.name}}
          </div>
          <div class="card-body">
            <p>Vreme: {{ reservation.time }} h</p>
            <p>Trajanje: {{ reservation.massage_id.length }} min</p>
            <p>Cena masaze: {{ reservation.massage_id.price }} RSD</p>
            <p>Maser: {{ reservation.masseur_id.user.first_name }} {{ reservation.masseur_id.user.last_name }}</p>
            <div class="text-center">
              <button class="btn btn-outline-danger" @click="deleteReservation(reservation)">Otkazi</button>
            </div>
          </div>
        </div>
        </div>
      </div>
      <div @click="togglePastReservations"
        style="border:1px solid;cursor:pointer;background-color:gray;max-width: 450px;">
        <h5 style="margin: auto;">Past Reservations</h5>
        <div v-if="pastReservations">
          <div v-for="reservationDate in sortedReservations.filter(x => Date.parse(x) < Date.parse(currentDate))"
            :key="reservationDate" style="border:1px solid;min-height:50px">
            <h3>{{ reservationDate }}</h3>
            <div
              v-for="reservation in reservations.filter(x => x.date === reservationDate).sort(function (a, b) { return a.time.localeCompare(b.time) })"
              :key="reservation">
              <div style="border:1px solid">
                {{ reservation.time }}
                {{ reservation.massage_id.length }} min
                {{ reservation.massage_id.type }}
                {{ reservation.massage_id.price }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-4">
      <div class="container" v-if="this.readonlyInfo && userInfo">
        <div class="card">
          <div class="card-body" style="margin: 0 15px 0 15px;">
            <h5 class="card-title" style="text-align:center; margin-bottom: 30px;">Moji podaci</h5>

            <p><b>Ime:</b> &nbsp;&nbsp;{{ userInfo.user.first_name }}</p>

            <p><b>Prezime:</b> &nbsp;&nbsp;{{ userInfo.user.last_name }}</p>

            <p><b>Email:</b> &nbsp;&nbsp;{{ userInfo.user.email }}</p>

            <p><b>Broj telefon:</b> &nbsp;&nbsp;{{ userInfo.phone_number }}</p>

            <p><b>Datum rodjenja:</b> &nbsp;&nbsp;{{ userInfo.birth_date }}</p>

            <p><b>Adresa:</b> &nbsp;&nbsp;{{ userInfo.location }}</p>
            <button class=" btn btn-outline-primary"
              style="color: #fff; background: #33cabb !important; border: none; margin-top: 0px !important; width: 100%;"
              v-if="this.readonlyInfo" @click="this.readonlyInfo = false">Izmeni</button>
          </div>


        </div>
      </div>
      <div v-if="!this.readonlyInfo && this.userInfoForm">
        <form>
          <div class="card" style="padding: 30px;">
            <div class="form-group">
              <label class="form-label" style="margin-bottom: 3px !important;">Ime: </label>
              <input type="text" class="form-control form-control-sm" placeholder="Unesite Ime"
                v-model="this.userInfoForm.user.first_name" style="margin-bottom: -10px;">
            </div>
            <div class="form-group">
              <label class="form-label" style="margin-bottom: 3px !important;">Prezime: </label>
              <input type="text" class="form-control form-control-sm" placeholder="Unesite Prezime"
                v-model="this.userInfoForm.user.last_name" style="margin-bottom: -10px;">
            </div>
            <div class="form-group">
              <label class="form-label" style="margin-bottom: 3px !important;">Email: </label>
              <input type="email" class="form-control form-control-sm" placeholder="Unesite Email"
                v-model="this.userInfoForm.user.email" style="margin-bottom: -10px;">
            </div>
            <div class="form-group">
              <label class="form-label" style="margin-bottom: 3px !important;">Broj telefona: </label>
              <input type="text" class="form-control form-control-sm" placeholder="Unesite Broj telefona"
                v-model="this.userInfoForm.phone_number" style="margin-bottom: -10px;">
            </div>
            <div class="form-group">
              <label class="form-label" style="margin-bottom: 3px !important;">Datum rodjenja: </label>
              <input type="text" class="form-control form-control-sm" placeholder="Unesite datum rodjenja"
                v-model="this.userInfoForm.birth_date" style="margin-bottom: -10px;">
            </div>
            <div class="form-group">
              <label class="form-label" style="margin-bottom: 3px !important;">Adresa: </label>
              <input type="text" class="form-control form-control-sm" placeholder="Unesite Adresu"
                v-model="this.userInfoForm.location" style="margin-bottom: -10px;">
            </div>
            <div>
              <button type="submit" class="btn btn-primary" data-dismiss="modal" aria-label="Save"
              @click="saveInfo" style="margin: 10px 10px 0 0;color: #fff; background: #33cabb !important; border: none;">Save</button>
            <button class="btn btn-secondary" aria-label="Close" @click="readonlyInfo = true" style="margin: 11px 0 0 0; border: none;">Discard</button>
            </div>
            
          </div>
        </form>
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
      userInfoForm: null,
      futureTermins: 'green'
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
    window.addEventListener("beforeunload", event => {
      if (this.readonlyInfo) return
      event.preventDefault()
      event.returnValue = ""
    })
    this.$store.dispatch('initialToken')
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
      this.$router.push({ name: 'HomeView'})
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
    