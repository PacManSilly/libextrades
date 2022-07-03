<script setup>
/* eslint-disable */
import { RouterView } from 'vue-router';
</script>

<template>
    <div class="w-full h-full min-h-full">

        <div class="w-full h-full flex flex-col">

            <div class="flex flex-col gap-2 pb-5 mt-10 mb-10 border-b border-slate-700 lg:mt-0">
                <h1 class="text-white text-4xl font-black">Copy Expert Traders</h1>
                <span class="text-slate-600 font-normal tracking-wide">Select one expert trader to become your manager</span>
            </div>

            <div class="w-full h-full flex items-center justify-center">
                <RouterView />
            </div>

        </div>
    </div>
</template>