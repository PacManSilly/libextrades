<script setup>
/* eslint-disable */
import btclogo from '../assets/images/btc.png';
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';

</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <div class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10">
                <h1 class="text-white font-black text-2xl md:text-4xl">Update Your Profile</h1>
            </div>

            <div class="flex gap-2">
                <img :src="btclogo" class="h-20 w-20 rounded-full overflow-hidden">
                <input type="file" name="mugshot" id="mugshot" class="self-end transition-all duration-150 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-slate-100 file:text-blue-600 hover:file:bg-slate-100 hover:text-slate-100">
            </div>

            <div class="w-full grid gap-3 grid-cols-1 mt-5 md:grid-cols-2">
                <AppInputField label="First Name" />
                <AppInputField label="Last Name" />
            </div>

            <div class="w-full grid gap-3 grid-cols-1 md:grid-cols-2">
                <AppInputField label="Other Name" />
                <AppInputField label="Date of Birth" type="date" />
            </div>

            <div>
                <AppInputField label="Phone Number" placeholder="+1 (555) 123-4567" />
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Save" class="w-full md:w-1/4" />
            </div>

        </div>

    </div>
</template>