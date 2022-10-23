<template>
    <header>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <router-link :to="{ name: 'HomeView' }" class="navbar-brand">Masaza<b>Balans</b></router-link>
            <!-- Collection of nav links, forms, and other content for toggling -->
            <div id="navbarCollapse" class="collapse navbar-collapse justify-content-start">
                <div class="navbar-nav">
                    <a href="#" class="nav-item nav-link">Contact</a>
                    <router-link :to="{ name: 'UserPortal' }" v-if="loggedIn">My portal</router-link> 
                </div>
                <form class="navbar-form form-inline">
                    <div class="input-group search-box">
                        <input type="text" id="search" class="form-control" placeholder="Search here...">
                        <div class="input-group-append">
                            <span class="input-group-text">
                                <i class="material-icons">&#xE8B6;</i>
                            </span>
                        </div>
                    </div>
                </form>
                <div class="navbar-nav ml-auto action-buttons" v-if="!loggedIn">
                    <div class="nav-item dropdown">
                        <a href="#" data-toggle="dropdown" class="nav-link dropdown-toggle mr-4">Login</a>
                        <div class="dropdown-menu action-form">
                            <form @submit.prevent="login">
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="Username" required="required"
                                        v-model="credentials.username">
                                </div>
                                <div class="form-group">
                                    <input type="password" class="form-control" placeholder="Password"
                                        required="required" v-model="credentials.password" @input="this.wrongCredentials=''">
                                        <a style="color:red">{{wrongCredentials}}</a>
                                </div>
                                <input type="submit" class="btn btn-primary btn-block" value="Login">
                                <div class="text-center mt-2">
                                    <a href="#">Forgot Your password?</a>
                                </div>
                            </form>
                        </div>
                    </div>
                    <div class="nav-item dropdown">
                        <a href="#" data-toggle="dropdown" class="btn btn-primary dropdown-toggle sign-up-btn">Sign
                            up</a>
                        <div class="dropdown-menu action-form">
                            <form @submit.prevent="signup">
                                <p class="hint-text">Fill in this form to create your account!</p>
                                <div class="form-group">
                                    <input type="text" class="form-control" placeholder="Username" required="required"
                                        v-model="signupCredentials.username">
                                </div>
                                <div class="form-group">
                                    <input type="password" class="form-control" placeholder="Password"
                                        required="required" v-model="signupCredentials.password">
                                </div>
                                <div class="form-group">
                                    <input type="password" class="form-control" placeholder="Confirm Password"
                                        required="required" v-model="signupCredentials.passwordConfirm">
                                    <p style="color: red;" class="hint-text" v-if="!matchingPasswords">Passwords are not
                                        matching!</p>

                                </div>
                                <div class="form-group">
                                    <label class="form-check-label"><input type="checkbox" required="required"> I accept
                                        the <a href="#">Terms &amp; Conditions</a></label>
                                </div>
                                <ul v-for="error in signupErrors" :key="error" style="color:red">
                                    <li>{{error}}</li>
                                </ul>
                                <input type="submit" class="btn btn-primary btn-block" value="Sign up" :disabled="!matchingPasswords">
                            </form>
                        </div>
                    </div>
                </div>
                <div v-if="loggedIn" class="nav-item dropdown" style="margin-right:0;margin-left:auto">
                    <a href="#" id="reset" data-toggle="dropdown" class="nav-link dropdown-toggle mr-4">Reset Password</a>
                    <div class="dropdown-menu action-form">
                        <form @submit.prevent="resetPassword">
                            <div class="form-group">
                                <input type="password" class="form-control" placeholder="Old Password"
                                    required="required" v-model="reset.oldPassword" @input="this.wrongPassword = ''">
                                <a style="color:red">{{wrongPassword}}</a>
                            </div>
                            <div class="form-group">
                                <input type="password" class="form-control" placeholder="New Password"
                                    required="required" v-model="reset.newPassword">
                            </div>
                            <div class="form-group">
                                <input type="password" class="form-control" placeholder="Confirm Password"
                                    required="required" v-model="reset.newPasswordConfirm">
                            </div>
                            <p style="color: red;" class="hint-text" v-if="!matchingResetPasswords">Passwords are not
                                        matching!</p>
                            <input type="submit" class="btn btn-primary btn-block" value="Reset Password" :disabled="!matchingResetPasswords">
                        </form>
                    </div>
                </div>
                <div v-if="loggedIn" style="margin-right:0;margin-left:0">
                    <button class="nav-item btn btn-primary" @click.prevent="logout">Logout</button>
                </div>
            </div>
        </nav>
    </header>
</template>
  
<script>
import MassageService from '@/services/MassageService'
import axios from 'axios'

export default {
    name: 'HeaderHome',
    data() {
        return {
            credentials: {
                username: '',
                password: ''
            },
            reset: {
                oldPassword: '',
                newPassword: '',
                newPasswordConfirm: '',
            },
            signupCredentials: {
                username: '',
                password: '',
                passwordConfirm: '',
            },
            errors: [],
            wrongPassword: '',
            wrongCredentials: '',
            signupErrors: []
        }
    },
    methods: {
        signup() {
            if (this.signupCredentials.password == this.signupCredentials.passwordConfirm) {
                this.$store.dispatch('signupDjango', this.signupCredentials)
                .then(response => {
                    console.log(response)
                }
                )
                .catch(error => {
                    if(JSON.parse(error.response.request.responseText).username) {
                        this.signupErrors = JSON.parse(error.response.request.responseText).username
                    }
                    else if(JSON.parse(error.response.request.responseText).password) {
                        this.signupErrors = JSON.parse(error.response.request.responseText).password 
                    }

                })
            }
        },
        login() {
            if (this.credentials.username === 'nikola') {
                MassageService.loginDjango(this.credentials)
                    .then(response => {
                        if (response.status === 200) {
                            MassageService.loginAdmin(this.credentials)
                                .then(window.location.href = "http://localhost:8000/admin")

                        }
                    })

            }
            else {
                this.$store.dispatch('loginDjango', this.credentials).catch(error => {
                    console.log(error)
                    this.wrongCredentials = 'Wrong credentials'
                })
            }
        },
        logout() {
            this.$store.state.token = ''
            this.$store.state.isAuthenticated = false
            localStorage.removeItem("token")
        },
        resetPassword() {
            if (this.reset.newPassword === this.reset.newPasswordConfirm) {
                const body = {
                    "token": localStorage.getItem('token'),
                    "oldPassword": this.reset.oldPassword,
                    "newPassword": this.reset.newPassword
                }
                MassageService.verifyPassword(body)
                    .then(response => {
                        if (response.status === 200) {
                            document.querySelector('#reset').click()
                            this.reset.oldPassword = ''
                            this.reset.newPassword = ''
                            this.reset.newPasswordConfirm = ''
                        }
                    })
                    .catch(error => {
                        console.log(error)
                        this.wrongPassword = 'Wrong password'
                    }
                    )
            }
        }
    },
    computed: {
        matchingPasswords() {
            if (this.signupCredentials.password == this.signupCredentials.passwordConfirm || this.signupCredentials.passwordConfirm === '') {
                return true
            }
            else {
                return false
            }
        },
        matchingResetPasswords() {
            if (this.reset.newPassword == this.reset.newPasswordConfirm || this.reset.newPasswordConfirm === '') {
                return true
            }
            else {
                return false
            }
        },
        loggedIn() {
            if (this.$store.state.token) {
                return true
            }
            else {
                return false
            }
        }
    },
    beforeCreate() {
    this.$store.dispatch('initialToken')
    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common['Authorization'] = 'Token' + token
    }
    else {
      axios.defaults.headers.common['Authorization'] = ''
    }
  },
}
// Prevent dropdown menu from closing when click inside the form
// $(document).on("click", ".action-buttons .dropdown-menu", function(e){
// 	e.stopPropagation();
// });
</script>
  
<style scoped>
body {
    font-family: 'Varela Round', sans-serif;
}

.form-control {
    box-shadow: none;
    font-weight: normal;
    font-size: 13px;
}

.navbar {
    background: #fff;
    padding-left: 16px;
    padding-right: 16px;
    border-bottom: 1px solid #dfe3e8;
    border-radius: 0;
}

.nav-link img {
    border-radius: 50%;
    width: 36px;
    height: 36px;
    margin: -8px 0;
    float: left;
    margin-right: 10px;
}

.navbar .navbar-brand {
    padding-left: 0;
    font-size: 20px;
    padding-right: 50px;
}

.navbar .navbar-brand b {
    color: #33cabb;
}

.navbar .form-inline {
    display: inline-block;
}

.navbar a {
    color: #888;
    font-size: 15px;
}

.search-box {
    position: relative;
}

.search-box input {
    padding-right: 35px;
    border-color: #dfe3e8;
    border-radius: 4px !important;
    box-shadow: none
}

.search-box .input-group-text {
    min-width: 35px;
    border: none;
    background: transparent;
    position: absolute;
    right: 0;
    z-index: 9;
    padding: 7px;
    height: 100%;
}

.search-box i {
    color: #a0a5b1;
    font-size: 19px;
}

.navbar .sign-up-btn {
    min-width: 110px;
    max-height: 36px;
}

.navbar .dropdown-menu {
    color: #999;
    font-weight: normal;
    border-radius: 1px;
    border-color: #e5e5e5;
    box-shadow: 0 2px 8px rgba(0, 0, 0, .05);
}

.navbar a,
.navbar a:active {
    color: #888;
    padding: 8px 20px;
    background: transparent;
    line-height: normal;
}

.navbar .navbar-form {
    border: none;
}

.navbar .action-form {
    width: 280px;
    padding: 20px;
    left: auto;
    right: 0;
    font-size: 14px;
}

.navbar .action-form a {
    color: #33cabb;
    padding: 0 !important;
    font-size: 14px;
}

.navbar .action-form .hint-text {
    text-align: center;
    margin-bottom: 15px;
    font-size: 13px;
}

.navbar .btn-primary,
.navbar .btn-primary:active {
    color: #fff;
    background: #33cabb !important;
    border: none;
}

.navbar .btn-primary:hover,
.navbar .btn-primary:focus {
    color: #fff;
    background: #31bfb1 !important;
}

.or-seperator {
    margin-top: 32px;
    text-align: center;
    border-top: 1px solid #e0e0e0;
}

.or-seperator b {
    color: #666;
    padding: 0 8px;
    width: 30px;
    height: 30px;
    font-size: 13px;
    text-align: center;
    line-height: 26px;
    background: #fff;
    display: inline-block;
    border: 1px solid #e0e0e0;
    border-radius: 50%;
    position: relative;
    top: -15px;
    z-index: 1;
}

.navbar .action-buttons .dropdown-toggle::after {
    display: none;
}

.form-check-label input {
    position: relative;
    top: 1px;
}

@media (min-width: 1200px) {
    .form-inline .input-group {
        width: 300px;
        margin-left: 30px;
    }
}

@media (max-width: 768px) {
    .navbar .dropdown-menu.action-form {
        width: 100%;
        padding: 10px 15px;
        background: transparent;
        border: none;
    }

    .navbar .form-inline {
        display: block;
    }

    .navbar .input-group {
        width: 100%;
    }
}
</style>
  