<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { useUserStore } from '../stores/user';
import { RouterLink } from 'vue-router';
import AppInputFieldVue from '../components/AppInputField.vue';
import AppButtonVue from '../components/AppButton.vue';
import IconLongLeftVue from '../components/icons/IconLongLeft.vue'
import AppLogoVue from '../components/AppLogo.vue'
import AppPasswordFieldVue from '../components/AppPasswordField.vue';

// store
const store = useUserStore()

// data
const email = ref(JSON.parse(window.localStorage.getItem('libex_email')));
const password = ref("");

// methods
const signIn = () => {
    const data = {
        username: email.value,
        password: password.value,
    }
    store.signIn(data)
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
        <div class="w-full flex flex-col gap-10 mt-20">

            <!-- start of header -->
            <header class="flex flex-col gap-2">
                <p class="text-2xl text-white font-black md:text-4xl">Sign In</p>
                <span class="text-sm text-slate-500">Sign into your LibExTrades account.</span>
            </header>

            <form @submit.prevent="signIn" class="w-full flex flex-col gap-5 md:gap-10">

                <!-- start of handle errors  -->
                <transition
                    enter-from-class="-translate-y-5 opacity-0"
                    enter-active-class="transitiona-ll duration-150"
                    leave-to-class="-translate-y-5 opacity-0"
                    leave-active-class="transitiona-ll duration-150">
                    <ul v-if="store.userSignIn.error || store.userSignIn.success" class="flex flex-col text-xs list-inside md:text-sm">
                        <li v-if="store.userSignIn.error" class="text-red-600">{{store.userSignIn.error}}</li>
                        <li v-if="store.userSignIn.success" class="text-green-600">Signed in successful. Redirecting...</li>
                    </ul>
                </transition>

                <!-- start of form fields -->
                <div class="flex flex-col gap-4">
                    <AppInputFieldVue v-model="email" type="email" placeholder="Enter email address..." label="Email Address" />
                    <AppPasswordFieldVue class="w-full" v-model="password" label="Password" />

                    <div class="w-full -mt-2">
                        <RouterLink :to="{name: 'forgotpassword'}" class="text-sm font-bold text-blue-500 transition-all duration-150 hover:text-blue-600">Forgot password?</RouterLink>
                    </div>
                </div>

                <!-- start of button -->
                <div class="w-full flex flex-col gap-3 items-center">
                    <div class="w-full">
                        <AppButtonVue name="Sign In" :loading="store.userSignIn.loading" />
                    </div>
                    <div class="flex items-center gap-2 text-xs md:text-sm">
                        <p class="text-xs font-normal text-slate-500">Don't have an account?</p>
                        <RouterLink :to="{name: 'signup'}" class="font-bold text-blue-500 transition-all duration-150 hover:text-blue-600">Sign Up</RouterLink>
                    </div>
                </div>
            </form>

        </div>
        
    </div>

</div>
</template>
