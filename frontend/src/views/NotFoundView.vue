<script setup>
/* eslint-disable */
import { useRouter } from 'vue-router';
import AppButton from '../components/AppButton.vue';

// router
const router = useRouter()

// methods
const navigateToHome = () => {
    router.push({name: 'home'})
}
</script>

<template>
    <div class="w-full h-screen min-h-full bg-slate-900">

        <div class="w-full h-full flex flex-col items-center justify-center lg:flex-row">

            <div class="flex flex-col items-center divide-y divide-slate-500 md:flex-row md:divide-x md:divide-y-0">
                <span class=" text-red-600 text-4xl font-black pb-2 md:pr-2 md:self-start md:text-6xl">404</span>
                <div class="flex flex-col gap-2 pt-2 md:pl-2">
                    <span class="text-white text-xl md:text-2xl">Page not found</span>
                    <span class="text-slate-500 font-normal text-xs md:text-sm">Please make sure the URL in the address bar is correct and try again</span>

                    <div class="flex self-start mt-5">
                        <AppButton @click.prevent="navigateToHome" name="Go back home" />
                    </div>
                </div>
            </div>

        </div>

    </div>
</template>