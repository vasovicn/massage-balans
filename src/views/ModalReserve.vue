<template>
    <div class="modal fade" id="myModal">
        <div class="modal-dialog">
            <div class="modal-content">

                <!-- Modal Header -->
                <div class="modal-header">
                    <h4 class="modal-title">Reserve {{massage.name}} massage</h4>
                    <button type="button" class="close" data-dismiss="modal">&times;</button>
                </div>

                <!-- Modal body -->
                <div class="modal-body">
                    <div>
                        <p>Price: {{massage.price}} RSD</p>
                        <p>Time: {{time}}h</p>
                        <p>length: {{massage.length}}min</p>
                    </div>
                    <form>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Enter your full name" v-model="reservation.name" >
                        </div>
                        <div class="form-group">
                            <input type="email" class="form-control" placeholder="Enter email" v-model="reservation.email" >
                        </div>
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Enter phone number" v-model="reservation.phone" >
                        </div>
                        <button type="submit" class="btn btn-primary" data-dismiss="modal" aria-label="Close" @click="sendReservation">Reserve</button>
                    </form>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'ModalReserve',
    data () {
        return {
            reservation: {
                name: '',
                email: '',
                phone: null
            }
        }
    },
    methods: {
        sendReservation() {
            this.$emit('submitReservation', this.reservation)
        }

    },
    props: ['massage', 'time']
};
</script>
<style>

</style>