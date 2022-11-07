<template>
    <div class="modal fade" id="resetPassword">
        <div class="modal-dialog">
            <div class="modal-content">

                <!-- Modal Header -->
                <div class="modal-header">
                    <h4 class="modal-title">Resetuj sifru</h4>
                    <button @click="this.email = null; this.username = ''" type="button" class="close"
                        data-dismiss="modal">&times;</button>
                </div>

                <!-- Modal body -->
                <div class="modal-body">
                    <form>
                        <p>Pronadji nalog</p>
                        <div class="form-group">
                            <input v-if="!email" type="text" class="form-control" placeholder="Unesite korisnicko ime"
                                v-model="username">
                        </div>
                        <p style="color: red;" v-if="message">{{ message }}</p>
                        <button style="background: #81bfaa !important;border: none;" v-if="!email" type="submit" class="btn btn-primary" aria-label="Close"
                            @click.prevent="searchUser">Pronadji</button>
                        <p v-if="email">Email za resetovanje sifre ce biti poslat na: {{ email }}</p>
                        <button style="background: #81bfaa !important;border: none;" type="submit" class="btn btn-primary" @click.prevent="sendEmail" v-if="email" data-dismiss="modal">Potvrdi</button>
                    </form>
                </div>

            </div>
        </div>
    </div>
</template>
<script>
import MassageService from '@/services/MassageService'
import $ from 'jquery'

export default {
    name: 'ModalResetPassword',
    data() {
        return {
            username: '',
            email: null,
            message: ''
        }
    },
    mounted() {
        $('#resetPassword').on('hidden.bs.modal', this.emptyData)
    },
    methods: {
        emptyData() {
            this.username = ''
            this.email = null
            this.message = ''
        },
        searchUser() {
            MassageService.searchUser(this.username)
                .then(response => {
                    if (response.status === 200) {
                        this.email = response.data
                        this.message = ''
                    }
                })
                .catch(error => {
                    console.log(error)
                    this.message = 'Korisnik sa tim korisnickim imenom nije pronadjen'
                })
        },
        sendEmail() {
            MassageService.sendResetEmail(this.email)
                .then(response => {
                    console.log(response)
                    this.$store.dispatch('showSuccessPopup', true)
                })
        }

    },
};
</script>