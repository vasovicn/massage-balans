<template>
    <div class="row" style="padding:30px">
      <div class="col-8" v-if="this.$store.state.isMasseur">
        <div style="margin-top: 78px;display: flex;justify-content: center;" v-if="sortedReservations.filter(x => Date.parse(x) < Date.parse(currentDate)).length === 0"><p style="font-size: x-large;">Istorija rezervacija nije dostupna</p></div>
        <div v-for="reservationDate in sortedReservations.filter(x => Date.parse(x) < Date.parse(currentDate))"
          :key="reservationDate" style="min-height:50px;">
          <div style="margin: 20px 0;">
            <h3>{{ reservationDate }}</h3>
          </div>
          <div class="row">
            <div class="card" style="width: 30%; margin: 10px;"
            v-for="reservation in reservations.filter(x => x.date === reservationDate).sort(function (a, b) { return a.time.localeCompare(b.time) })"
            :key="reservation.id">
            <div class="card-header" style="text-align: center; background-color: #81bfaa;font-size: larger;font-weight: 500;color: rgba(99, 103, 104, 0.99);">
              {{reservation.product_id.massage_id.name}}
            </div>
            <div class="card-body">
              <p>Vreme: {{ reservation.time }} h</p>
              <p>Trajanje: {{ reservation.product_id.length }} min</p>
              <p>Cena masaze: {{ reservation.product_id.price }} RSD</p>
              <p>Klijent: {{ reservation.user_id.user.first_name }} {{ reservation.user_id.user.last_name }}</p>
              <p>Telefon: {{ reservation.user_id.phone_number }}</p>
              <p>Email: {{ reservation.user_id.user.email }}</p>
            </div>
          </div>
          </div>
        </div>
      </div>
      <div class="col-8" v-else>
        <div style="margin-top: 78px;display: flex;justify-content: center;" v-if="sortedReservations.filter(x => Date.parse(x) < Date.parse(currentDate)).length === 0"><p style="font-size: x-large;">Istorija rezervacija nije dostupna</p></div>
        <div v-for="reservationDate in sortedReservations.filter(x => Date.parse(x) < Date.parse(currentDate))"
          :key="reservationDate" style="min-height:50px;">
          <div style="margin: 20px 0;">
            <h3>{{ reservationDate }}</h3>
          </div>
          <div class="row">
            <div class="card" style="width: 30%; margin: 10px;"
            v-for="reservation in reservations.filter(x => x.date === reservationDate).sort(function (a, b) { return a.time.localeCompare(b.time) })"
            :key="reservation.id">
            <div class="card-header" style="text-align: center; background-color: #81bfaa;font-size: larger;font-weight: 500;color: rgba(99, 103, 104, 0.99);">
              {{reservation.product_id.massage_id.name}}
            </div>
            <div class="card-body">
              <p>Vreme: {{ reservation.time }} h</p>
              <p>Trajanje: {{ reservation.product_id.length }} min</p>
              <p>Cena masaze: {{ reservation.product_id.price }} RSD</p>
              <p>Maser: {{ reservation.masseur_id.user.first_name }} {{ reservation.masseur_id.user.last_name }}</p>
              
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
                style="color: #fff; background: rgb(129, 191, 170) !important; border: none; margin-top: 0px !important; width: 100%;"
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
                @click="saveInfo" style="margin: 10px 10px 0 0;color: #fff; background: rgb(129, 191, 170) !important; border: none;">Save</button>
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
    name: 'PastReservations',
    data() {
      return {
        pastReservations: false,
        readonlyInfo: true,
        userInfoForm: null,
        futureTermins: 'green'
      }
    },
    props: ['event'],
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

  </style>
      