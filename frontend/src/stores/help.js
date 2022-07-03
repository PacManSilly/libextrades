/* eslint-disable */
import { defineStore } from "pinia";
import axios from "axios"


export const useHelp = defineStore({
    id: "help",
    state: () => ({
        password: {loading: false, success: null, error: null},
        verify: {loading: false, success: null, error: null}
    }),
    actions: {
        async forgotPassword(data) {
            this.password.loading = true
            this.password.success = null
            this.password.error = null

            await axios.post('auth/help/password/reset/', data)
                .then((resp) => {
                    this.password.success = resp.data.detail
                    this.password.loading = false
                    this.password.error = null

                    setTimeout(() => {
                        this.password.success = null
                    }, 3000);
                })
                .catch((err) => {
                    this.password.loading = false
                    this.password.success = null
                    this.userData.error = "An error occured."
                })
        },
        async resetPassword(data) {
            this.password.loading = true
            this.password.success = null
            this.password.error = null

            await axios.post(`auth/help/password/reset/confirm/${data.uid}/${data.token}/`, data)
                .then((resp) => {
                    this.password.success = resp.data.detail
                    this.password.loading = false
                    this.password.error = null
                    console.log(resp.data)

                    setTimeout(() => {
                        this.password.success = null
                        this.$router.push({name: 'signin'})
                    }, 3000);
                })
                .catch((err) => {
                    this.password.loading = false
                    this.password.success = null
                    if (err.response.data) this.password.error = "Password is to common"
                    else this.userData.error = "An error occured."
                    console.log(err.response.data)
                })
        },
        async verifyAccount(data) {
            this.verify.loading = true
            this.verify.success = null
            this.verify.error = null

            await axios.get(`api/verify-email/?token=${data.token}`)
                .then((resp) => {
                    this.verify.success = resp.data.detail
                    this.verify.loading = false
                    this.verify.error = null
                    console.log(resp.data)

                    setTimeout(() => {
                        this.verify.success = null
                        this.$router.push({name: 'home'})
                    }, 3000);
                })
                .catch((err) => {
                    this.verify.loading = false
                    this.verify.success = null
                    if (err.response.data.error) this.verify.error = err.response.data.error
                    else this.userData.error = "An error occured."
                    console.log(err.response.data)
                })
        },
    }
})