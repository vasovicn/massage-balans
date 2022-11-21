<template>
    <div style="display:flex;justify-content: space-around;margin-top: 100px;">
        <form>
            <div class="form-group">
                <input type="password" class="form-control" placeholder="Unesi novu sifru" v-model="password">
            </div>
            <div class="form-group">
                <input type="password" class="form-control" placeholder="Unesi novu sifru ponovo"
                    v-model="passwordRepeat">
            </div>
            <p style="color: red;" class="hint-text" v-if="!matchingResetPasswords">Passwords are not
                matching!</p>
            <p style="color:red" class="hint-text">{{wrongPassword}}</p>
            <button  type="submit" class="btn btn-primary" aria-label="Close"
                @click.prevent="resetPassword" :disabled="!matchingResetPasswords">Promeni</button>
        </form>
    </div>
</template>
    
<script>
import MassageService from '@/services/MassageService'

export default {
    name: 'ResetPassword',
    data() {
        return {
            password: '',
            passwordRepeat: '',
            wrongPassword: ''
        }
    },
    props: ['uidb64', 'token'],
    methods: {
        resetPassword() {
            if (this.password === this.passwordRepeat) {
                const body = {
                    "password": this.password,
                    "token": this.token,
                    "uidb64": this.uidb64
                }
                MassageService.resetPasswordEmail(body)
                    .then(response => {
                        if (response.status === 200) {
                            this.password = ''
                            this.passwordRepeat = ''
                            this.$router.push({ name: 'HomeView', hash: '#resetsuccess'})
                        }
                    })
                    .catch(error => {
                        console.log(error.response.data.password)
                        if (error.response.data.password) {
                            this.wrongPassword = error.response.data.password[0]

                        }
                    }
                    )
            }
        }
    },
    computed: {
        matchingResetPasswords() {
            if (this.password === this.passwordRepeat || this.passwordRepeat === '') {
                return true
            }
            else {
                return false
            }
        },
    }

}
</script>
    
<style>

</style>
    