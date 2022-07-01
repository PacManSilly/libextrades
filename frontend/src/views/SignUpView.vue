<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink, useRouter } from 'vue-router';
import AppInputFieldVue from '../components/AppInputField.vue';
import AppButtonVue from '../components/AppButton.vue';
import IconLongLeftVue from '../components/icons/IconLongLeft.vue'
import AppLogoVue from '../components/AppLogo.vue'
import AppPasswordFieldVue from '../components/AppPasswordField.vue';
import { useUserStore } from '@/stores/user';

// router
const router = useRouter()

// store
const store = useUserStore()
// store.$subscribe((mutation, state) => {
//     if (state.userSignUp.success) router.push({name: 'signin'})
// })

// data
const error = ref(null)
const fname = ref("");
const lname = ref("");
const oname = ref("");
const dob = ref("");
const email = ref("");
const phone = ref("");
const password1 = ref("");
const password2 = ref("");

// methods
const cleanPassword = () => {
    if (password2.value !== password1.value) {
        error.value = "Password does not match. Please retype your password"
        return false
    }
    else {
        error.value = null
        return true
    }
}

const signUp = () => {
    const data = {
        first_name: fname.value,
        last_name: lname.value,
        other_name: oname.value,
        dob: dob.value,
        email: email.value,
        phone: phone.value,
        password: password2.value,
    }

    if (cleanPassword()) store.signUp(data)
}
</script>

<template>
<div class="w-full h-full bg-slate-900">

    <div class="w-9/12 h-full min-h-[30rem] flex flex-col gap-10 py-20 items-center mx-auto md:w-1/2 lg:w-3/12">

        <!-- start of logo and back nav -->
        <div class="w-full flex items-center justify-between">
            <AppLogoVue />
            <RouterLink :to="{name: 'home'}" class="flex items-center gap-2 group">
                <IconLongLeftVue class="w-7 h-7 fill-slate-500 group-hover:animate-bounce-h" />
                <p class="text-blue-500 hover:text-blue-600">Home</p>
            </RouterLink>
        </div>

        <!-- start of sign in form  -->
        <div class="w-full flex flex-col gap-5 mt-10 md:gap-10">

            <!-- start of header -->
            <header class="flex flex-col gap-2">
                <p class="text-2xl text-white font-black md:text-4xl">Sign Up</p>
                <span class="text-sm text-slate-500">Let’s create your LibExTrades account.</span>
            </header>

            <form @submit.prevent="signUp" class="w-full flex flex-col gap-5">

                <!-- start of handle errors  -->
                <transition
                    enter-from-class="-translate-y-5 opacity-0"
                    enter-active-class="transitiona-ll duration-150"
                    leave-to-class="-translate-y-5 opacity-0"
                    leave-active-class="transitiona-ll duration-150">
                    <ul v-if="error || store.userSignUp.error || store.userSignUp.success" class="flex flex-col text-sm list-inside">
                        <li v-if="error || store.userSignUp.error" class="text-red-600">{{error || store.userSignUp.error}}</li>
                        <li v-if="store.userSignUp.success" class="text-green-600">Registration Successful. Redirecting...</li>
                    </ul>
                </transition>

                <!-- start of form fields -->
                <div class="flex flex-col gap-5">
                    <div class="flex flex-col gap-5 md:flex-row">
                        <AppInputFieldVue class="w-full" type="text" v-model="fname" label="First Name" />
                        <AppInputFieldVue class="w-full" type="text" v-model="lname" label="Last Name" />
                    </div>
                    <div class="flex flex-col gap-5 md:flex-row">
                        <AppInputFieldVue class="w-full" type="text" v-model="oname" label="Other Name" />
                        <AppInputFieldVue class="w-full" type="date" v-model="dob" label="Date of Birth" />
                    </div>
                    <div class="flex flex-col gap-5">
                        <AppInputFieldVue v-model="email" type="email" label="Email Address" />
                        <AppInputFieldVue v-model="phone" type="phone" label="Phone Number" placeholder="+1 (555) 123-4567" />
                    </div>
                    <div class="flex flex-col gap-5 md:flex-row">
                        <AppPasswordFieldVue class="w-full" v-model="password1" label="Password" />
                        <AppPasswordFieldVue class="w-full" v-model="password2" label="Confirm Password" />
                    </div>
                </div>

                <!-- start of button -->
                <div class="w-full flex flex-col gap-3 mt-4 items-center">
                    <div class="w-full">
                        <AppButtonVue name="Sign Up" :loading="store.userSignUp.loading" />
                    </div>
                    <div class="flex items-center gap-2 text-xs md:text-sm">
                        <p class="text-xs font-normal text-slate-500">Already have an account?</p>
                        <RouterLink :to="{name: 'signin'}" class="font-bold text-blue-500 transition-all duration-150 hover:text-blue-600">Sign In</RouterLink>
                    </div>
                </div>
            </form>

        </div>
        
    </div>

</div>
</template>
