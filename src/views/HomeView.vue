<template>
  <div v-show="showSuccessEmail" class="alert alert-success" style="margin: 10px 0 0 59%;position:absolute;z-index:100">
    Email za restovanje lozinke je uspesno poslat, ako niste primili pokusajte ponovo</div>
  <div v-show="showSuccessPassword" class="alert alert-success"
    style="margin: 10px 0 0 59%;position:absolute;z-index:100">Sifra uspesno resetovana, mozete se ulogovati sa novom
    sifrom</div>
  <div class="row" style="margin:80px">
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
import axios from 'axios'

export default {
  name: 'HomeView',
  components: {
    MassageList,
    MasseurList,
  },
  beforeCreate() {
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
    }
  },
  computed: {
    showSuccessEmail() {
      return this.$store.state.successEmail
    },
    showSuccessPassword() {
      return this.$store.state.successPassword
    },
  }
}
</script>
  
<style scoped>
@import'~bootstrap/dist/css/bootstrap.css'
</style>
  