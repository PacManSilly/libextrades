<script setup>
/* eslint-disable */
import { RouterLink, useRoute } from 'vue-router';
import { useHelp } from '../stores/help';
import IconLongLeft from '../components/icons/IconLongLeft.vue'
import AppLogo from '../components/AppLogo.vue'
import { onMounted } from 'vue';

// stores
const store = useHelp()

// route
const route = useRoute()

// data
const data = {token: route.query.token}

// methods
onMounted(() => {
    store.verifyAccount(data)
})
</script>

<template>
    <div class="w-full h-full min-w-full bg-slate-900">

        <div class="w-9/12 h-full min-h-[30rem] flex flex-col gap-10 py-20 items-center mx-auto md:w-1/2 lg:w-3/12">

            <!-- start of logo and back nav -->
            <div class="w-full flex items-center justify-between">
                <AppLogo />
                <RouterLink :to="{name: 'home'}" class="flex items-center gap-2 group">
                    <IconLongLeft class="w-7 h-7 fill-slate-500 group-hover:animate-bounce-h" />
                    <p class="text-blue-500 hover:text-blue-600">Home</p>
                </RouterLink>
            </div>

            <!-- start of sign in form  -->
            <div class="w-full flex flex-col gap-10 mt-20">

                <!-- start of header -->
                <header class="flex flex-col gap-2">
                    <p class="text-2xl text-white font-black md:text-4xl">Verify Your Account</p>
                </header>

                <p v-if="store.verify.error" class="text-red-600 text-lg font-bold">{{store.verify.error}}</p>
                <p v-else-if="store.verify.success" class="text-green-600 text-lg font-bold">{{store.verify.success}} Redirecting...</p>
                <p v-else class="text-slate-500 text-lg font-bold">Verifying your account. Please wait...</p>
            </div>

        </div>

    </div>
</template>