/* eslint-disable */
import { defineStore } from "pinia";
import { useUserInvestment } from "./investment";
import { useUserWithdrawal } from "./withdrawal";
import { useUserTrader } from "./trader";
import axios from "axios";


export const useUserStore = defineStore({
    id: "user",
    state: () => ({
        userData: {loading: true, data: JSON.parse(localStorage.getItem('libex_user')), error: null},
        userSignUp: {loading: false, data: null, success: false, error: null},
        userSignIn: {loading: false, token: JSON.parse(localStorage.getItem('libex_token')), success: false, redirect: null, error: null},
        profileUpdate: {modal: false, loading: false, success: null, error: null}
    }),
    actions: {
        async signUp(data) {
            this.userSignUp.loading = true
            await axios.post("users/new/", data, {headers: {"Content-Type": "multipart/form-data"}})
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
            // store
             const investmentStore = useUserInvestment()
             const withdrawalStore = useUserWithdrawal()
             const traderStore = useUserTrader()

            this.userSignIn.loading = true
            this.userSignIn.error = null
            await axios.post("auth/token/login/", {...data})
                .then((resp) => {
                    this.userSignIn.error = null
                    this.userSignIn.loading = false
                    localStorage.setItem('libex_token', JSON.stringify(resp.data['access_token']))
                    localStorage.setItem('libex_email', JSON.stringify(data['username']))
                    this.userSignIn.token = JSON.parse(localStorage.getItem('libex_token'))
                    this.userSignIn.success = true

                    // get all users data
                    this.getMe()
                    investmentStore.getInvestments()
                    withdrawalStore.getWithdrawals()
                    traderStore.getTraders()

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
                })
        },
        async updateMe(data) {
            this.profileUpdate.loading = true
            this.profileUpdate.success = null
            this.profileUpdate.error = null

            await axios.put('users/me/update/', data, {headers: {'Content-Type': 'multipart/form-data', 'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
                .then((resp) => {
                    this.profileUpdate.loading = false
                    this.profileUpdate.error = null
                    this.profileUpdate.success = "Updated successfully. redirecting..."
                    
                    setTimeout(() => {
                        this.profileUpdate.modal = false
                        this.profileUpdate.success = null
                    }, 3000);
                    
                    // call getMe() action
                    this.getMe()
                })
                .catch((err) => {
                    this.profileUpdate.loading = false
                    this.profileUpdate.modal = true
                    this.profileUpdate.success = null
                    if (err.response.status == 401) this.signOut()
                    else this.userData.error = "An error occured."
                })
        },
        async changePassword(data) {
            this.profileUpdate.loading = true
            this.profileUpdate.success = null
            this.profileUpdate.error = null

            axios.post('users/me/change/password/', data, {headers: {'Authorization': `Bearer ${JSON.parse(localStorage.getItem('libex_token'))}`}})
                .then((resp) => {
                    this.profileUpdate.loading = false
                    this.profileUpdate.error = null
                    this.profileUpdate.success = `${resp.data.detail} redirecting...`
                    
                    setTimeout(() => {
                        this.profileUpdate.modal = false
                        this.profileUpdate.success = null
                    }, 3000);
                })
                .catch((err) => {
                    this.profileUpdate.loading = false
                    this.profileUpdate.modal = true
                    this.profileUpdate.success = null
                    if (err.response.status == 401) this.signOut()
                    else if (err.response.data.new_password2) this.profileUpdate.error = "Password is to common"
                    else this.userData.error = "An error occured."
                })
        }
    }
})