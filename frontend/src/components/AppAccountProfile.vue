<script setup>
/* eslint-disable */
import { useUserStore } from "../stores/user";
import IconSetting from "./icons/IconSetting.vue";
import { computed } from "vue";

// stores
const store = useUserStore()

// computed
const fullName = computed(() => {
    const fname = store.userData.data.first_name
    const lname = store.userData.data.last_name
    const oname = store.userData.data.other_name

    return fname + " " + lname + " " + oname
})

// created hooks
store.getMe()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <!-- loading -->
        <div v-if="store.userData.loading" class="w-full h-full flex items-center justify-center">
            <IconSetting class="w-10 h-10 fill-slate-600 md:w-20 md:h-20" />
        </div>

        <!-- error -->
        <div v-else-if="store.userData.error" class="w-full h-full flex items-center justify-center">
            <span class="text-red-600 text-sm md:text-lg">{{store.userData.error}}</span>
        </div>

        <!-- success -->
        <div v-else class="w-full h-full flex flex-col">

            <div class="pb-5 mt-10 mb-10 border-b border-slate-700 md:mt-0">
                <h1 class="text-white text-4xl font-black">Investor Profile</h1>
            </div>

            <div class="flex flex-col items-center gap-10 md:items-start">
                
                <div class="flex flex-col gap-1">
                    <div class="w-40 h-40 flex items-center justify-center bg-slate-800 overflow-hidden">
                        <img v-if="store.userData.data.mugshot" :src="store.userData.data.mugshot" alt="Picture" class="w-full h-full object-cover object-center">
                        <p v-else class="text-6xl font-black text-white">S</p>
                    </div>
                    <p class="text-white text-xl font-medium">{{fullName}}</p>
                </div>

                <div class="flex flex-col gap-2 w-full md:w-9/12 lg:w-6/12 xl:w-5/12">
                    <div class="flex justify-between">
                        <span class="text-slate-500 text-sm font-medium">Account ID:</span>
                        <span class="text-xs text-white bg-cyan-600 p-1 rounded md:text-sm">{{store.userData.data.id}}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-500 text-sm font-medium">Email Address:</span>
                        <span class="text-xs text-white bg-blue-600 p-1 rounded md:text-sm">{{store.userData.data.email}}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-500 text-sm font-medium">Phone:</span>
                        <span class="text-xs text-white bg-purple-600 p-1 rounded md:text-sm">{{store.userData.data.phone}}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-500 text-sm font-medium">Country:</span>
                        <span class="text-xs text-white bg-black p-1 rounded md:text-sm">{{store.userData.data.country || 'None'}}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-500 text-sm font-medium">Investment Plan:</span>
                        <span class="text-xs text-white bg-pink-600 p-1 rounded md:text-sm">{{store.userData.data.investment_plan}}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-500 text-sm font-medium">Investment Currency:</span>
                        <span class="text-xs text-white bg-orange-600 p-1 rounded md:text-sm">Bitcoin</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-slate-500 text-sm font-medium">Account Status:</span>
                        <span :class="store.userData.data.is_verified ? 'bg-green-600':'bg-red-600'" class="text-xs text-white p-1 rounded md:text-sm">{{store.userData.data.is_verified ? 'Verified':'Unverified'}}</span>
                    </div>
                    
                </div>

            </div>
        

        </div>
    
    </div>
</template>