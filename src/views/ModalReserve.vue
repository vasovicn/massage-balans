<template>
    <div class="modal fade" id="myModal">
        <div class="modal-dialog">
            <div v-if="massage && time" class="modal-content">

                <!-- Modal Header -->
                <div class="modal-header">
                    <h4 class="modal-title" v-if="!this.paymentStep">Rezervisi {{ massage.name }} masazu</h4>
                    <h4 class="modal-title" v-else>Placanje</h4>
                    <button id="close" type="button" class="close" data-dismiss="modal">&times;</button>
                </div>

                <!-- Modal body -->


                <div class="modal-body" v-if="!this.paymentStep">
                    <div class="row">
                        <div class="col-6">
                            <p>Datum: {{ date }}</p>
                            <p>Vreme: {{ time }}h</p>
                        </div>
                        <div class="col-6">
                            <p>Cena: {{ massage.price }} RSD</p>
                            <p>Trajanje: {{ massage.length }}min</p>
                        </div>
                    </div>
                    <form @submit.prevent="sendReservation">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Unesite ime i prezime"
                                v-model="reservation.name" required="required">
                        </div>
                        <div class="form-group">
                            <input type="email" class="form-control" placeholder="Unesite email adresu"
                                v-model="reservation.email" required="required">
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Unesite broj telefona"
                                v-model="reservation.phone" required="required">
                        </div>
                        <div class="form-group">
                            <input type="submit" class="button" value="Rezervisi" />
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'ModalReserve',
    data() {
        return {
            reservation: {
                name: '',
                email: '',
                phone: null,
            },
        }
    },
    methods: {
        async sendReservation() {
                await this.$emit('submitReservation', this.reservation)
                document.querySelector('#close').click()
        },
        nextStep() {
            this.paymentStep = true
        },
        backStep() {
            this.paymentStep = false
        },
        PayMassage() {
            console.log('dsadasd')
        }
    },
    computed: {
        massage() {
            return this.$store.state.massage
        },
        time() {
            return this.$store.state.time
        },
        date() {
            return this.$store.state.currentMassageDate
        }
    },
};
</script>
<style scoped>
.button {
    background-color: #81bfaa;
    border-radius: 18px;
    /* box-shadow: #81bfaa 0 -25px 18px -14px inset, #81bfaa 0 1px 2px, #81bfaa 0 2px 4px, #81bfaa 0 4px 8px, #81bfaa 0 8px 16px, #81bfaa 0 16px 32px; */
    color: white;
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
    float: right;
}

.button:hover {
    transform: scale(1.05);
}
#card-number {
    height: 37px;
    border: 1px solid;
    border-color: #00000042;
    width: 162px;
    padding: 8px;
    display: flex;
    margin-bottom: 5px;
    padding-left: 16px;
    border-radius: 3px;
    align-content: center;
    justify-content: center;
}
#cvv {
    height: 37px;
    border: 1px solid;
    border-color: #00000042;
    width: 58px;
    padding: 8px;
    display: flex;
    margin-bottom: 5px;
    padding-left: 16px;
    border-radius: 3px;
    align-content: center;
    justify-content: center;
}
#expiration-date {
    height: 37px;
    border: 1px solid;
    border-color: #00000042;
    width: 88px;
    padding: 8px;
    display: flex;
    margin-bottom: 5px;
    padding-left: 16px;
    border-radius: 3px;
    align-content: center;
    justify-content: center;
}
</style>