<template>
    <div style="margin-top:90px">
        <div class="col-8" style="margin-left: auto;">
            <RouterLink :to="{ name: 'FeautureReservations' }">Predstojece Masaze</RouterLink>  |
            <RouterLink :to="{ name: 'PastReservations' }">Istorija masaza</RouterLink>
        </div>
        <RouterView :event="event" style="padding-top: 5px;"/>
    </div>
</template>
      
<script>
import axios from 'axios'


export default {
    name: 'LayoutPortal',
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
            this.$router.push({ name: 'HomeView' })
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
.router-link-exact-active {
    color: green
  }
a {
    color: black;
}
</style>
      