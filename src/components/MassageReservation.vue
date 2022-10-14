<template>
    <div v-if="massageID">
        <p>Trajanje masaze: {{massage.length}} min</p>
        <p> Cena masaze: {{massage.price}} RSD</p>
        <p>{{massage.info}}</p>
        <input id="date_picker" :min="dateMin" type="date" v-model="date" @change="changedDate" />
        <TimeComponent v-if="date && clicked" :date="date" :massage="massage" :currentTime="currentTime"
            :currentDate="dateMin" @clicked-time="clickedTime" />
        <div class="choosen-time" v-if="date && !clicked" @click="this.clicked = !this.clicked">
            Vreme:{{time}}
        </div>
        <button v-if="date && !clicked" class="button" data-toggle="modal" data-target="#myModal">Posalji
            rezervaciju</button>
        <ModalReserve @submitReservation="sendReservation" :massage="massage" :time="time" />

    </div>
</template>
    
<script>
import TimeComponent from '@/components/TimeComponent.vue'
import ModalReserve from '@/views/ModalReserve.vue'

import { uuid } from 'vue-uuid';

export default {
    name: 'MassageReservation',
    data() {
        return {
            date: "",
            clicked: false,
            time: "",
            currentTime: "",
        }
    },
    components: {
        TimeComponent,
        ModalReserve
    },
    props: ['massageID'],
    created() {
        this.$store.dispatch('fetchMassageDjango', this.massageID)
        this.timeMin()

    },
    computed: {
        massage() {
            return this.$store.state.massage
        },
        dateMin() {
            var today = new Date();
            var dd = String(today.getDate()).padStart(2, '0');
            var mm = String(today.getMonth() + 1).padStart(2, '0');
            var yyyy = today.getFullYear();
            today = yyyy + '-' + mm + '-' + dd;
            return today
        }
    },
    methods: {
        clickedTime(time) {
            this.clicked = !this.clicked
            this.time = time
        },
        changedDate() {
            if (!this.clicked) {
                this.clicked = !this.clicked
            }
        },
        sendReservation(reservation) {
            const reservedTermin = {
                "id": uuid.v4(),
                "date": this.date,
                "time": this.time,
                "length": this.massage.length,
                "type": this.massage.name,
                "client": {
                    'name': reservation.name,
                    'email': reservation.email,
                    'phone': reservation.phone,
                }
            }
            this.$store.dispatch('postReservationDjango', reservedTermin)
            // this.$router.push({ name: 'MassageConfirmation', params: {id: reservation.id}})
            this.$emit('reserved')
        },
        timeMin() {
            var today = new Date();
            var hours = String(today.getHours()).padStart(2, '0');
            var minutes = String(today.getMinutes()).padStart(2, '0');

            var time = hours + ':' + minutes
            this.currentTime = time
        },
        closeModal() {
            this.toggleModal = false
        }
    }
}
</script>
<style scoped>
.massage {
    display: flex;
    flex-direction: column;
    align-items: center;
    /* border:1px solid; */
    min-width: 200px;
    max-width: 700px;
    max-height: 500px;
    margin: auto;
    padding: 10px
}

.time {
    margin-top: 10px;
    padding: 3px;
    min-height: 20px;
}

.time:hover {
    background-color: rgb(218, 218, 218);
    cursor: pointer;
    border-radius: 10px;
}

.button {
    background-color: #c2fbd7;
    border-radius: 100px;
    box-shadow: rgba(44, 187, 99, .2) 0 -25px 18px -14px inset, rgba(44, 187, 99, .15) 0 1px 2px, rgba(44, 187, 99, .15) 0 2px 4px, rgba(44, 187, 99, .15) 0 4px 8px, rgba(44, 187, 99, .15) 0 8px 16px, rgba(44, 187, 99, .15) 0 16px 32px;
    color: green;
    cursor: pointer;
    display: inline-block;
    font-family: CerebriSans-Regular, -apple-system, system-ui, Roboto, sans-serif;
    padding: 7px 20px;
    text-align: center;
    text-decoration: none;
    transition: all 250ms;
    border: 0;
    font-size: 16px;
    user-select: none;
    -webkit-user-select: none;
    touch-action: manipulation;
}

.button:hover {
    box-shadow: rgba(44, 187, 99, .35) 0 -25px 18px -14px inset, rgba(44, 187, 99, .25) 0 1px 2px, rgba(44, 187, 99, .25) 0 2px 4px, rgba(44, 187, 99, .25) 0 4px 8px, rgba(44, 187, 99, .25) 0 8px 16px, rgba(44, 187, 99, .25) 0 16px 32px;
    transform: scale(1.05);
}

.choosen-time {
    padding: 10px;
}

.choosen-time:hover {
    transform: scale(1.05);
    background-color: #c2fbd7;
    cursor: pointer;
    border-radius: 5px;
}
</style>
  
    