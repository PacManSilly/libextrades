/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios";


export const useUserStore = defineStore({
    id: "user",
    state: () => ({
        userData: {loading: true, data: JSON.parse(localStorage.getItem('libex_user')), error: null},
        userSignUp: {loading: false, data: null, success: false, error: null},
        userSignIn: {loading: false, token: JSON.parse(localStorage.getItem('libex_token')), success: false, redirect: null, error: null},
    }),
    actions: {
        async signUp(data) {
            this.userSignUp.loading = true
            await axios.post("users/new/", {...data})
                .then((resp) => {
                    this.userSignUp.error = null
                    this.userSignUp.loading = false
                    localStorage.setItem('libex_email', JSON.stringify(resp.data.email))
                    this.userSignUp.success = true

                    // redirect to login page
                    this.$router.push({name: 'signin'})
                })
                .catch((err) => {
                    this.userSignUp.loading = false
                    if (err.response.data['email']) this.userSignUp.error = "Email address belongs to another account"
                    else this.userSignUp.error = "An error occured, please try again."
                    this.userSignUp.success = false
                })
        },
        async signIn(data) {
            this.userSignIn.loading = true
            await axios.post("auth/token/login/", {...data})
                .then((resp) => {
                    this.userSignIn.error = null
                    this.userSignIn.loading = false
                    localStorage.setItem('libex_token', JSON.stringify(resp.data['access_token']))
                    localStorage.setItem('libex_email', JSON.stringify(data['username']))
                    this.userSignIn.token = JSON.parse(localStorage.getItem('libex_token'))
                    this.userSignIn.success = true

                    // then redirect to initially requested page or home
                    this.$router.push(this.userSignIn.redirect || {name: 'home'})
                    this.userSignIn.success = false
                })
                .catch((err) => {
                    this.userSignIn.loading = false
                    if (err.response.data.non_field_errors) this.userSignIn.error = "Incorrect Email/Password"
                    else this.userSignIn.error = "An error occured, please try agin."
                    this.userSignIn.success = false
                })
        },
        async signOut() {
            localStorage.removeItem('libex_token')
            localStorage.removeItem('libex_user')
            this.$router.push({name: 'home'})
        },
        async getMe() {
            this.userData.loading = true
            await axios.get("users/me/", {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
                .then((resp) => {
                    this.userData.error = null
                    this.userData.loading = false
                    localStorage.setItem('libex_user', JSON.stringify(resp.data))
                    this.userData.data = JSON.parse(localStorage.getItem('libex_user'))
                })
                .catch((err) => {
                    this.userData.loading = false
                    if (err.response.status == 401) this.signOut()
                    else this.userData.error = "An error occured."
                    console.log(err.response)
                })
        }
    }
})