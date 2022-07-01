<script setup>
/* eslint-disable */
import AppInputField from './AppInputField.vue';
import AppButton from './AppButton.vue';

</script>

<template>
    <div class="w-full h-full min-h-full mx-auto">

        <div class="w-full h-full flex flex-col gap-5 md:w-10/12">

            <div class="text-center mb-10">
                <h1 class="text-white font-black text-2xl md:text-4xl">Update Your Email Address</h1>
            </div>

            <div class="w-full flex flex-col gap-1">
                <AppInputField label="Email Address" type="email" />
                <span class="text-slate-500 text-sm font-medium">Your current email address: samuel.l.jackson@gmail.com</span>
            </div>

            <div class="w-full flex md:justify-end">
                <AppButton name="Save" class="w-full md:w-1/4" />
            </div>

        </div>

    </div>
</template>