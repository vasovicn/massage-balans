<template>
  <ModalReserve @submitReservation="sendReservation"/>
  <div v-show="showSuccessMassageReservation" class="alert alert-success" style="margin: 90px 0 0 59%;position:absolute;z-index:100">
    Uspesno ste rezervisali termin</div>
  <div v-show="showSuccessEmail" class="alert alert-success" style="margin: 90px 0 0 59%;position:absolute;z-index:100">
    Email za restovanje lozinke je uspesno poslat, ako niste primili pokusajte ponovo</div>
  <div v-show="showSuccessPassword" class="alert alert-success"
    style="margin: 90px 0 0 59%;position:absolute;z-index:100">Sifra uspesno resetovana, mozete se ulogovati sa novom
    sifrom</div>
  <div class="row" style="margin:90px">
    <div class="col-8">
      <MassageList />
    </div>
    <div class="col-1" @click="focusOUT" />
    <div class="col-3">
      <MasseurList />
    </div>
  </div>
</template>
  
<script>
import MassageList from '@/components/MassageList.vue'
import MasseurList from '@/components/MasseurList.vue'
import ModalReserve from '@/views/ModalReserve.vue'
import axios from 'axios'
import { uuid } from 'vue-uuid';


export default {
  name: 'HomeView',
  components: {
    MassageList,
    MasseurList,
    ModalReserve
  },
  beforeCreate() {
    this.$store.dispatch('fetchMasseuers')
      .catch(error => {
        console.log(error)
      })
    if (this.$route.hash === '#resetsuccess') {
      this.$store.dispatch('passwordReseted', true)
      this.$router.push({name: 'HomeView'})
    }
    this.$store.dispatch('initialToken')
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
  methods: {

    focusOUT() {
      this.$store.dispatch('setSelectedMassage', null)
    },
    sendReservation(reservation) {
            const reservedTermin = {
                "id": uuid.v4(),
                "date": this.$store.state.currentMassageDate,
                "time": this.$store.state.time,
                "length": this.massage.length,
                "type": this.massage.name,
                "client": {
                  'name': reservation.name,
                  'email': reservation.email,
                  'phone': reservation.phone,
                },
                "masseur_id": parseInt(this.$store.state.currentMasseur.id)
            }
            this.$store.dispatch('postReservationDjango', reservedTermin)
            this.$store.dispatch('setSelectedMassageButton', true)
            this.$store.commit('SET_SELECTED_MASSAGE', false)
            window.scrollTo(0,0);
        },
  },
  computed: {
    showSuccessEmail() {
      return this.$store.state.successEmail
    },
    showSuccessPassword() {
      return this.$store.state.successPassword
    },
    showSuccessMassageReservation() {
      return this.$store.state.successMassageReserved
    },
    massage() {
      return this.$store.state.massage
    }
  }
}
</script>
  
<style scoped>
@import'~bootstrap/dist/css/bootstrap.css'
</style>
  