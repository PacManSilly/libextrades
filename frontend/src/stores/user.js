/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios";

// axios settings
axios.defaults.baseURL = "http://127.0.0.1:8000/api/";
// axios.defaults.baseURL = "http://192.168.43.208:8000/api/";
// axios.defaults.baseURL = "http://192.168.1.102:8000/api/";
axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.withCredentials = true;
axios.defaults.timeout = 9000;


export const useUserStore = defineStore({
    id: "user",
    state: () => ({
        userData: null,
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
                    this.userSignIn.success = true

                    //redirect to initially requested page or home
                    this.$router.push(this.userSignIn.redirect || {name: 'home'})
                })
                .catch((err) => {
                    this.userSignIn.loading = false
                    if (err.response.data.non_field_errors) this.userSignIn.error = "Incorrect Email/Password"
                    else this.userSignIn.error = "An error occured, please try aagin."
                    this.userSignIn.success = false
                })
        },
        async signOut() {
            localStorage.removeItem('libex_token')
            this.$router.push({name: 'home'})
        }
    }
})