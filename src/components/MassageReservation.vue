<template>
    <div v-if="massageID">
        <p>Trajanje masaze: {{ massage.length }} min</p>
        <p> Cena masaze: {{ massage.price }} RSD</p>
        <!-- <select v-if="masseuers" @change="onChange($event)">
                <option disabled selected value> -- select masseur -- </option>
                <option v-for="masseur in masseuers" :key="masseur" :value="masseur.id">
                    {{ masseur.user.first_name }}
                </option>
            </select> -->
        <!-- <div class="carousel-container">
            <input type="radio" name="slider" id="item-1" checked>
            <input type="radio" name="slider" id="item-2">
            <input type="radio" name="slider" id="item-3">
            <div class="cards">
                <label class="card" for="item-1" id="song-1">
                    <img class="carousel-img"
                        src="https://images.unsplash.com/photo-1530651788726-1dbf58eeef1f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=882&q=80"
                        alt="song">
                </label>
                <label class="card" for="item-2" id="song-2">
                    <img class="carousel-img"
                        src="https://images.unsplash.com/photo-1559386484-97dfc0e15539?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1234&q=80"
                        alt="song">
                </label>
                <label class="card" for="item-3" id="song-3">
                    <img class="carousel-img"
                        src="https://images.unsplash.com/photo-1533461502717-83546f485d24?ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60"
                        alt="song">
                </label>
            </div>
        </div> -->
        <div class="carousel-container">
            <input v-for="(masseur, index) in masseuers" :key="index" type="radio" name="slider"
                :id="'item-' + parseInt(parseInt(index) + parseInt(1))" :checked="index === 0"/>
            <div class="cards">
                <label v-for="(masseur, index) in masseuers" :key="index" class="card"
                    :for="'item-' + parseInt(parseInt(index) + parseInt(1))"
                    :id="'song-' + parseInt(parseInt(index) + parseInt(1))">
                    <img class="carousel-img" :src="masseur.photo_url" alt="song" @click="this.selectedMasseur = masseur">
                </label>
            </div>
        </div>
        <div>{{selectedMasseur.user.first_name}}</div>
        <br />
        <div style="margin-bottom:10px">
            <input id="date_picker" :min="dateMin" type="date" v-model="date" @change="changedDate" />
        </div>
        <div class="btns-background" v-if="date && clicked">
            <button @click="this.timePeriod = [7, 12]" class="btn-abc btn-left"
                :style="{ backgroundColor: this.timePeriod[0] === 7 ? 'white' : '#f1f1f1' }">Morning</button>
            <button @click="this.timePeriod = [11, 17]" class="btn-abc"
                :style="{ backgroundColor: this.timePeriod[0] === 11 ? 'white' : '#f1f1f1' }">Afternoon</button>
            <button @click="this.timePeriod = [16, 22]" class="btn-abc btn-right"
                :style="{ backgroundColor: this.timePeriod[0] === 16 ? 'white' : '#f1f1f1' }">Evening</button>
        </div>
        <TimeComponent v-if="date && clicked" :date="date" :massage="massage" :currentTime="currentTime"
            :masseur_id="selectedMasseur.id" :currentDate="dateMin" @clicked-time="clickedTime"
            :timePeriod="this.timePeriod" />
        <div class="choosen-time" v-if="date && !clicked" @click="this.clicked = !this.clicked">
            Vreme:{{ time }}
        </div>
        <button v-if="!this.$store.state.isAuthenticated && date && !clicked" class="button" data-toggle="modal"
            data-target="#myModal">Posalji
            rezervaciju</button>
        <button v-if="this.$store.state.isAuthenticated && date && !clicked" class="button"
            @click="sendReservation">Posalji
            rezervaciju</button>
        <ModalReserve @submitReservation="sendReservation" :massage="massage" :time="time" />

        <!-- <div id="carouselExampleControls" class="carousel slide" data-ride="carousel" data-interval="false">
            <div class="carousel-inner">
                <div class="carousel-item active">
                    <p>A</p>
                </div>
                <div class="carousel-item">
                    <p>B</p>
                </div>
                <div class="carousel-item">
                    <p>C</p>
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-target="#carouselExampleControls"
                data-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-target="#carouselExampleControls"
                data-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </button>
        </div> -->
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
            masseur_id: 1,
            timePeriod: [7, 12],
            selectedMasseur: this.$store.state.masseuers[0]
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
        },
        masseuers() {
            // var masseursPointer = null
            // let masseuers = this.$store.state.masseuers
            // for (let i = 0; i < masseuers.legth; i++) {
            //     if (i === masseuers.length - 1) {
            //         masseursPointer.push(i, masseuers[0])
            //     }
            //     else {
            //         masseursPointer.push(i, masseuers[i + 1])
            //     }
            // }

            // let currentMasseurIndex = currentMasseurIndex % masseuers.length;
            // let x = []
            // for (let [index, [key, value]] of Object.entries(Object.entries(masseursPointer))) {
            //     let endIndex = (currentMasseurIndex + index) % masseuers.length
            //     if (key >= currentMasseurIndex && key <= endIndex) {
            //         x.push(value)
            //     }
            // }

            // return x

            return this.$store.state.masseuers
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
            }
            if (reservation.name != undefined) {
                reservedTermin["client"] = {
                    'name': reservation.name,
                    'email': reservation.email,
                    'phone': reservation.phone,
                }
            }
            else {
                reservedTermin["token"] = this.$store.state.token
            }
            reservedTermin['masseur_id'] = parseInt(this.selectedMasseur.id)
            this.$store.dispatch('postReservationDjango', reservedTermin)
            // this.$router.push({ name: 'MassageConfirmation', params: {id: reservation.id}})
            this.$emit('reserved')
            this.$emit('fold')
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
        },
    }
}
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css?family=DM+Sans:400,500,700&display=swap");


input[type=radio] {
    display: none;
}

.card {
    position: absolute;
    width: 100%;
    height: 150px;
    left: 0;
    right: 0;
    margin: auto;
    transition: transform 0.4s ease;
    cursor: pointer;
}

.carousel-container {
    margin: auto;
    margin-top: -120px;
    margin-bottom: -20px;
    width: 200px;
    height: 300px;
    transform-style: preserve-3d;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.cards {
    position: relative;
    width: 70%;
    height: 15%;
}

.carousel-img {
    width: 100%;
    height: 100%;
    border-radius: 10px;
    object-fit: cover;
}

#item-1:checked~.cards #song-3,
#item-2:checked~.cards #song-1,
#item-3:checked~.cards #song-2 {
    transform: translatex(-40%) scale(0.8);
    opacity: 0.4;
    z-index: 0;
}

#item-1:checked~.cards #song-2,
#item-2:checked~.cards #song-3,
#item-3:checked~.cards #song-1 {
    transform: translatex(40%) scale(0.8);
    opacity: 0.4;
    z-index: 0;
}

#item-1:checked~.cards #song-1,
#item-2:checked~.cards #song-2,
#item-3:checked~.cards #song-3 {
    transform: translatex(0) scale(1);
    opacity: 1;
    z-index: 1;
}

#item-1:checked~.cards #song-1 img,
#item-2:checked~.cards #song-2 img,
#item-3:checked~.cards #song-3 img {
    box-shadow: 0px 0px 5px 0px rgba(81, 81, 81, 0.47);
}

.player {
    background-color: #fff;
    border-radius: 8px;
    min-width: 320px;
    padding: 16px 10px;
}

.upper-part {
    position: relative;
    display: flex;
    align-items: center;
    margin-bottom: 12px;
    height: 36px;
    overflow: hidden;
}

.play-icon {
    margin-right: 10px;
}

.song-info {
    width: calc(100% - 32px);
    display: block;
}

.song-info .title {
    color: #403d40;
    font-size: 14px;
    line-height: 24px;
}

.sub-line {
    display: flex;
    justify-content: space-between;
    width: 100%;
}

.subtitle,
.time {
    font-size: 12px;
    line-height: 16px;
    color: #c6c5c6;
}

.time {
    font-size: 12px;
    line-height: 16px;
    color: #a5a5a5;
    font-weight: 500;
    margin-left: auto;
}

.progress-bar {
    height: 3px;
    width: 100%;
    background-color: #e9efff;
    border-radius: 2px;
    overflow: hidden;
}

.progress {
    display: block;
    position: relative;
    width: 60%;
    height: 100%;
    background-color: #2992dc;
    border-radius: 6px;
}

.info-area {
    width: 100%;
    position: absolute;
    top: 0;
    left: 30px;
    transition: transform 0.4s ease-in;
}

#item-2:checked~.player #test {
    transform: translateY(0);
}

#item-2:checked~.player #test {
    transform: translateY(-40px);
}

#item-3:checked~.player #test {
    transform: translateY(-80px);
}

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

.btn-abc {
    margin: 5px 0px 5px 0px;
    width: 20%;
    border: none;
    border-radius: 5px;
    background-color: #f1f1f1;
    width: 100%;
}

.btn-abc-selected {
    background-color: white;
}

.btns-background {
    background-color: #f1f1f1;
    border-radius: 5px;
    width: 310px;
    margin: 0 auto;
    display: inline-flex;
}

.btn-left {
    margin-left: 5px;
}

.btn-right {
    margin-right: 5px;
}
</style>
    