<script setup>
/* eslint-disable */
import { useUserStore } from '../stores/user';

// stores
const store = useUserStore()
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 pb-5 mt-10 mb-10 border-b border-slate-700 lg:mt-0">
                <h1 class="text-white text-4xl font-black">Referral</h1>
                <span class="text-slate-600 font-normal tracking-wide">Refer your friends and family and earn commissions.</span>
            </div>

            <div class="w-full flex flex-col gap-10 mt-10 items-start justify-between pb-10 md:gap-20 md:justify-center lg:flex-row">

                <div class="w-full flex flex-col gap-10 mx-auto md:w-9/12 lg:w-7/12">

                    <div class="flex flex-col gap-3 bg-slate-800 p-8 rounded">

                        <div class="flex justify-between text-slate-600">
                            <div class="flex flex-col items-center gap-1">
                                <span class="text-4xl font-black md:text-8xl">0</span>
                                <span class="font-medium">Referrals</span>
                            </div>
                            <div class="flex flex-col items-center gap-1">
                                <span class="text-4xl font-black md:text-8xl">0</span>
                                <span class="font-medium">My Rank</span>
                            </div>

                        </div>

                        <div>
                            <div class="flex flex-col items-center gap-3">
                                <span class="text-sm font-medium text-slate-600">Referral Link</span>
                                <span class="text-xs font-medium text-slate-100">https://libextrades.com/signup?refid={{store.userData.data.id}}</span>
                            </div>
                        </div>
                    
                    </div>

                    <div class="flex flex-col gap-3">
                        <span class="text-sm text-center text-slate-400 font-normal">
                            Gain free promotion upgrade with each ascending affiliate rank, your next rank will unlock with 3 successful referrals.
                        </span>

                        <ul class="list-disc list-inside text-sm text-slate-600">
                            <li>Rank 0 - 7% commission for every deposit + $2 bonus for reference registration</li>
                            <li>Rank 1 - 9% commission for every deposit + $2 bonus for reference registration</li>
                            <li>Rank 2 - 11% commission for every deposit + $2 bonus for reference registration</li>
                        </ul>
                    </div>

                </div>

            </div>
        
        </div>

    </div>
</template>