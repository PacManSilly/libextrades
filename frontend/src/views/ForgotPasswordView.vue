<script setup>
/* eslint-disable */
import { ref } from 'vue';
import { RouterLink } from 'vue-router';
import AppInputFieldVue from '../components/AppInputField.vue';
import AppButtonVue from '../components/AppButton.vue';
import IconLongLeftVue from '../components/icons/IconLongLeft.vue'
import AppLogoVue from '../components/AppLogo.vue'

const error = ref(false)
const email = ref("");
const password = ref("");
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
        <div class="w-full flex flex-col gap-10 mt-20">

            <!-- start of header -->
            <header class="flex flex-col gap-2">
                <p class="text-2xl text-white font-black md:text-4xl">Reset your password</p>
                <span class="text-sm text-slate-500">Provide the email address linked to your account.</span>
            </header>

            <form @submit.prevent class="w-full flex flex-col gap-5 md:gap-10">

                <!-- start of handle errors  -->
                <ul v-if="error" class="flex flex-col text-sm text-red-500 list-inside list-disc">
                    <li>error holder</li>
                </ul>

                <!-- start of form fields -->
                <div class="flex flex-col gap-4">
                    <AppInputFieldVue v-model="email" type="email" placeholder="Enter email address..." label="Email Address" />
                </div>

                <!-- start of button -->
                <div class="w-full flex flex-col gap-3 items-center">
                    <div class="w-full">
                        <AppButtonVue name="Reset my password" />
                    </div>
                    <div class="flex items-center gap-2 text-xs md:text-sm">
                        <p class="text-xs font-normal text-slate-500">Back to</p>
                        <RouterLink :to="{name: 'signin'}" class="font-bold text-blue-500 transition-all duration-150 hover:text-blue-600">Sign In</RouterLink>
                    </div>
                </div>
            </form>

        </div>
        
    </div>

</div>
</template>
