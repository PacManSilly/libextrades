<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import AppInputFieldVue from '../components/AppInputField.vue';
import AppButtonVue from '../components/AppButton.vue';
import IconLongLeftVue from '../components/icons/IconLongLeft.vue'
import AppLogoVue from '../components/AppLogo.vue'
import AppPasswordFieldVue from '../components/AppPasswordField.vue';

const error = ref(false)
const fname = ref("");
const lname = ref("");
const oname = ref("");
const dob = ref("");
const email = ref("");
const password1 = ref("");
const password2 = ref("");
const loading = ref(false);
</script>

<template>
<div class="w-full h-full bg-slate-900">

    <div class="w-9/12 h-full min-h-[30rem] flex flex-col gap-10 py-20 items-center mx-auto md:w-1/2 lg:w-3/12">

        <!-- start of logo and back nav -->
        <div class="w-full flex items-center justify-between">
            <AppLogoVue />
            <RouterLink :to="{name: 'home'}" class="flex items-center gap-2 group">
                <IconLongLeftVue class="group-hover:animate-bounce-h" />
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

            <form @submit.prevent class="w-full flex flex-col gap-5">

                <!-- start of handle errors  -->
                <ul v-if="error" class="flex flex-col text-sm text-red-500 list-inside list-disc">
                    <li>Password do not match</li>
                </ul>

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
                    <div>
                        <AppInputFieldVue v-model="email" type="email" label="Email Address" />
                    </div>
                    <div class="flex flex-col gap-5 md:flex-row">
                        <AppPasswordFieldVue class="w-full" v-model="password1" label="Password" />
                        <AppPasswordFieldVue class="w-full" v-model="password2" label="Confirm Password" />
                    </div>
                </div>

                <!-- start of button -->
                <div class="w-full flex flex-col gap-3 mt-4 items-center">
                    <div class="w-full">
                        <AppButtonVue name="Sign Up" />
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
